#!/usr/bin/env python3.5
# coding=utf-8
# Licensed Materials - Property of IBM®
# Copyright IBM® Corp. 2015,2017
"""Submit for submission of SPL applications.

The main function is submitSplApp to submit an SPL Application
to a Streaming Analytics service or IBM® Streams instance for execution.

usage: submitSPL.py [-h] --main_composite MAIN_COMPOSITE --project_dir
                    PROJECT_DIR [--job_name JOB_NAME] [--job_group JOB_GROUP]
                    [--data_directory DATA_DIRECTORY] --service_name
                    SERVICE_NAME --credentials_file CREDENTIALS_FILE
                    [--param_file PARAM_FILE]
                    [--toolkits_list_file TOOLKITS_LIST_FILE]

Submit SPL Application to IBM® Cloud Streaming Service

optional arguments:
  -h, --help            show this help message and exit
  --main_composite MAIN_COMPOSITE SPL Main composite with namespace i.e. com.ibm.streams::MainApp
  --project_dir PROJECT_DIR SPL application project directory
  --job_name JOB_NAME   Job name to appear in Streams console
  --job_group JOB_GROUP Job group, this must exist in the Streams instance to successfully submit
  --data_directory DATA_DIRECTORY SPL application data directory
  --service_name SERVICE_NAME Name of the IBM® Cloud Streaming service
  --credentials_file CREDENTIALS_FILE File containing the JSON of IBM® Cloud Streaming service credentials
  --param_file PARAM_FILE SPL parameters file with json array i.e.
                        [ { "name": "param1", "type": "rstring", "value": "paramValue1"}, ...]
  --toolkits_list_file TOOLKITS_LIST_FILE List of toolkits of dependencies

"""
import sys
import argparse
import streamsx.topology.topology
import streamsx.spl.op
import streamsx.topology.context
import streamsx.spl.toolkit
import streamsx.spl.types
import json
import os
'''
'''

def processParamFile(spl_main_param_file):
    splParams = {}
    try:
        jsonParams = json.load(open(spl_main_param_file))
    except Exception as err:
        print('ERROR : While processing spl_main_param_file : ', spl_main_param_file)
        print('Run-time error ', err)
        sys.exit(1)

    p = ''
    try:
        for p in jsonParams:
            if 'type' in p:
                exec('splParams[ p[\'name\'] ] = streamsx.spl.types.' + p['type'] + '(p[\'value\'])')
            else:
                splParams[p['name']] = p['value']
    except Exception as err:
        print('ERROR : While processing spl_main_param_file : ', spl_main_param_file)
        print('Error in the entry ->', p)
        print('Run-time error ', err)
        sys.exit(2)

    return splParams

def processToolkits(dep_toolkits):
    tkList =[]
    for tk in open(dep_toolkits):
        tk = tk.split('#')[0]
        tk = tk.replace(' ', '')
        tk = tk.rstrip()
        tk = tk.strip(' ')
        if len(tk) > 0 :
            if isToolkitDir(tk) :
                tkList.append(tk)
            else :
                print('ERROR : Could not find the toolkit directory : '+tk)
                print('it is specified in toolkit list file : ', dep_toolkits)
                sys.exit(4)

    return tkList

def isToolkitDir(tk):
    return (os.path.exists(tk) and os.path.isdir(tk))

def checkMainProjDir(dir):
    if not isToolkitDir(dir):
        print('ERROR : Could not find the main SPL project directory : ' + dir)
        sys.exit(4)


def submitSplApp(spl_main_composite,
                 spl_main_project_dir,
                 streaming_service_name,
                 service_credentials_filename,
                 spl_params=None,
                 dep_toolkits_list=None,
                 job_name=None,
                 job_group=None,
                 data_directory=None):
    '''
    :param spl_main_composite:  Must contain the namespace and main composite name i.e. com.ibm.streams::MainApp
    :param spl_main_project_dir: The Streams application project directory
    :param streaming_service_name: Name of the IBM® Cloud Streaming service
    :param service_credentials_filename: File containing the JSON of IBM® Cloud Streaming service credentials
    :param spl_params: SPL parameters dictionary loaded from file with json array as following
                        [ { "name": "param1", "type": "rstring", "value": "paramValue1"},...]
    :param dep_toolkits_list: List of toolkits of dependencies
    :param job_name: Job name to appear in Streams console
    :param job_group: Job group, this must exist in the Streams instance to successfully submit
    :param data_directory: Application data directory
    :return: SubmissionResult: Result of the submission. For details of what is contained see the :py:class:`ContextTypes`
            constant passed as `ctxtype`.
    '''
    # Topology object
    topo = streamsx.topology.topology.Topology(spl_main_composite.split('::')[-1])

    # ==================================================
    # IBM® Cloud Streaming Service Context Configuration
    # ==================================================
    try :
        credentials = json.load(open(service_credentials_filename))
    except Exception as err:
        print('ERROR : While processing service_credentials_filename : ', service_credentials_filename)
        print('Run-time error ', err)
        sys.exit(3)

    vs = {'streaming-analytics': [{'name': streaming_service_name, 'credentials': credentials}]}
    cfg = {}
    cfg[streamsx.topology.context.ConfigParams.VCAP_SERVICES] = vs
    cfg[streamsx.topology.context.ConfigParams.SERVICE_NAME] = streaming_service_name
    # job_name=None, job_group=None, preload=False, data_directory=None
    job_config = streamsx.topology.context.JobConfig(job_name=job_name, job_group=job_group, data_directory=data_directory)
    job_config.add(cfg)
    # ========================
    #    Toolkit Dependencies
    # ========================

    streamsx.spl.toolkit.add_toolkit(topo, spl_main_project_dir)

    if dep_toolkits_list is not None:
        for toolkit in dep_toolkits_list:
            streamsx.spl.toolkit.add_toolkit(topo, toolkit)

    # ===============
    #    Invoke SPL
    # ===============
    splMain = streamsx.spl.op.Invoke(topo, spl_main_composite, params=spl_params)

    # ===============
    #    Submit
    # ===============
    # submit(ctxtype, graph, config=None, username=None, password=None)
    # Submit the topology to to executed - STANDALONE, DISTRIBUTED, BLUEMIX
    # streamsx.topology.context.submit("DISTRIBUTED", topo)
    ctx = streamsx.topology.context.submit('STREAMING_ANALYTICS_SERVICE', topo, config=cfg)
    print('Submitted job to service:', streaming_service_name)
    return ctx


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Submit SPL Application to IBM® Cloud Streaming Service')
    parser.add_argument('--main_composite', help="SPL Main composite with namespace i.e. com.ibm.streams::MainApp", required=True )
    parser.add_argument('--project_dir', help="SPL application project directory", required=True )
    parser.add_argument('--job_name', help="Job name to appear in Streams console", default=None, required=False )
    parser.add_argument('--job_group', help="Job group, this must exist in the Streams instance to successfully submit", default=None, required=False )
    parser.add_argument('--data_directory', help="SPL application data directory", default=None, required=False)
    parser.add_argument('--service_name', help="Name of the IBM® Cloud Streaming service", required=True)
    parser.add_argument('--credentials_file', help="File containing the JSON of IBM® Cloud Streaming service credentials", required=True)
    parser.add_argument('--param_file', help='''SPL parameters file with json array i.e. 
        [ { "name": "param1", "type": "rstring", "value": "paramValue1"}, ...]''', default=None, required=False)
    parser.add_argument('--toolkits_list_file', help="List of toolkits of dependencies", default=None, required=False)

    args = parser.parse_args()

    spl_params = None
    dep_toolkits_list = None

    print("Submitting the application "+ args.main_composite +" with the following parameters:")
    print("  - main_composite     : " + args.main_composite)
    print("  - project_dir        : " + args.project_dir)
    if args.job_name is not None: print("  - job_name           : " + args.job_name)
    if args.job_group is not None: print("  - job_group          : " + args.job_group)
    if args.data_directory is not None: print("  - data_directory     : " + args.data_directory)
    print("  - service_name       : " + args.service_name)
    print("  - credentials_file   : " + args.credentials_file)
    if args.param_file is not None:
        print("  - param_file         : " + args.param_file)
        spl_params = processParamFile(args.param_file)
        for k,v in spl_params.items():
            print('   ->   '+k + ' = '+str(v))

    if args.toolkits_list_file is not None:
        print("  - toolkits_list_file : " + args.toolkits_list_file)
        dep_toolkits_list = processToolkits(args.toolkits_list_file)
        for tk in dep_toolkits_list:
            print('   ->   '+tk)


    # Assert the project directory exists
    assert isToolkitDir(args.project_dir), 'ERROR : Could not find the main SPL project directory : %s'%args.project_dir
    spl_main_project_dir = args.project_dir

    submitSplApp(args.main_composite, spl_main_project_dir, args.service_name, args.credentials_file,
                 spl_params, dep_toolkits_list, args.job_name, args.job_group, args.data_directory)

