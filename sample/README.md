# Sample Clickstream Applicaion
This sample application is composed of several Streaming analytics micro services. The current version is composed of the following :

* MessageHubIngest: Ingests data though Message Hub - from a simple flow designer application running in DSX
* ClkStrmEnrich: This little component does some basic data enrichment
* ClickstreamAggregates: Computes server layers of aggregates
* ClkStrmElasticSink: Sinks the aggregates into Elasticsearch after necessary transformations
 
# Architectural components need to run in IBM Cloud 
To run end-to-end this application requires three architectural components in the IBM Cloud 
1. Message Hub
2. Streaming Analytics
3. Elasticsearch + Kibana 

### dependency :
https://github.com/IBMStreams/streamsx.elasticsearch

## How to build ?
Before attempting to build this components of thie applicaion, download and build the Streams elasticsearch toolkit.

The `Makefile` in the root of this project can build all the components is one shot buy simply running:
```bash
make
```
