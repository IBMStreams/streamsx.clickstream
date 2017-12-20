#!/usr/bin/env bash
PROJ_DIR=../sample/001_Clickstream_MessageHub_Ingest
args=(
--job_name cs_ingest
--main_composite com.ibm.streamsx.clickstream.ingest::MessageHubIngest
--param_file $PROJ_DIR/etc/SplParams.json
--project_dir $PROJ_DIR
--service_name streaming-analytics-yf
--toolkits_list_file $PROJ_DIR/etc/depToolkits.lst
--credentials_file $PROJ_DIR/IBMCloudStreamingServiceCredentials.json
)
./submitSPL.py ${args[@]}

