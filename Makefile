.PHONY: all

all : com.ibm.streamsx.spl.util com.ibm.streamsx.clickstream Types MessageHubIngest ClkStrmEnrich ClickstreamAggregates ClkStrmElasticSink

Types :
	@echo '########################################'
	@echo ' Building' $@
	@echo '########################################'
	cd sample/000_Clickstream_DSX_Types && $(MAKE)
	
MessageHubIngest : Types com.ibm.streamsx.spl.util
	@echo '########################################'
	@echo ' Building' $@
	@echo '########################################'
	cd sample/001_Clickstream_MessageHub_Ingest && $(MAKE)

OfflineIngest : Types com.ibm.streamsx.spl.util
	@echo '########################################'
	@echo ' Building' $@
	@echo '########################################'
	cd sample/001_Clickstream_Offline_Ingest && $(MAKE)

ClkStrmEnrich : Types com.ibm.streamsx.spl.util 
	@echo '########################################'
	@echo ' Building' $@
	@echo '########################################'
	cd sample/002_Clickstream_Enrich && $(MAKE)

ClickstreamAggregates : Types com.ibm.streamsx.clickstream com.ibm.streamsx.spl.util
	@echo '########################################'
	@echo ' Building' $@
	@echo '########################################'
	cd sample/003_Clickstream_Aggregates && $(MAKE)

ClkStrmElasticSink : Types com.ibm.streamsx.clickstream com.ibm.streamsx.spl.util
	@echo '########################################'
	@echo ' Building' $@
	@echo '########################################'
	cd sample/008_Clickstream_Sink_Elasticsearch && $(MAKE)
	
com.ibm.streamsx.clickstream :
	@echo '########################################'
	@echo ' Building' $@
	@echo '########################################'
	cd com.ibm.streamsx.clickstream && $(MAKE)

com.ibm.streamsx.spl.util :
	@echo '########################################'
	@echo ' Building' $@
	@echo '########################################'
	cd com.ibm.streamsx.spl.util && $(MAKE)

clean :
	cd sample/000_Clickstream_DSX_Types && $(MAKE) clean
	$(MAKE) clean -C sample/001_Clickstream_MessageHub_Ingest
	cd sample/002_Clickstream_Enrich && $(MAKE) clean 
	cd sample/003_Clickstream_Aggregates && $(MAKE) clean 
	cd sample/008_Clickstream_Sink_Elasticsearch && $(MAKE) clean
	cd sample/001_Clickstream_Offline_Ingest && $(MAKE) clean