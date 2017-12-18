.PHONY: all distributed clean 


NS=com.ibm.streamsx.clickstream.Aggregates
APP=ClickstreamAggregates

SPL_MAIN_COMPOSITE = $(NS)::$(APP)
STREAMS_DEFAULT_OUTPUT_DIR=../../output/$(APP)

SPLC_FLAGS ?= -a --output-directory=$(STREAMS_DEFAULT_OUTPUT_DIR)

SPLC = $(STREAMS_INSTALL)/bin/sc
SPL_CMD_ARGS ?= 

# Toolkit dependencies 
SPLC_TOOLKIT_CLICKSTREAM_DSX_TYPES=../000_Clickstream_DSX_Types
SPLC_TOOLKIT_COM.IBM.STREAMSX.SPL.UTIL=../../com.ibm.streamsx.spl.util
SPLC_TOOLKIT_COM.IBM.STREAMSX.CLICKSTREAM=../../com.ibm.streamsx.clickstream
SPLC_TOOLKIT_COM.IBM.STREAMSX.JSON=$(STREAMS_INSTALL)/toolkits/com.ibm.streamsx.json

# List of all dependencies toolkits 
SPLC_TOOLKITS=$(SPLC_TOOLKIT_CLICKSTREAM_DSX_TYPES):$(SPLC_TOOLKIT_COM.IBM.STREAMSX.SPL.UTIL):$(SPLC_TOOLKIT_COM.IBM.STREAMSX.MESSAGEHUB):$(SPLC_TOOLKIT_COM.IBM.STREAMSX.JSON):$(SPLC_TOOLKIT_COM.IBM.STREAMSX.CLICKSTREAM)

# Add toolkits to the compiler flags
SPLC_FLAGS+= -t $(SPLC_TOOLKITS)

all: distributed

distributed:
	@mkdir -p $(STREAMS_DEFAULT_OUTPUT_DIR)
	$(SPLC) $(SPLC_FLAGS) -M $(SPL_MAIN_COMPOSITE) $(SPL_CMD_ARGS)

clean: 
	$(SPLC) $(SPLC_FLAGS) -C -M $(SPL_MAIN_COMPOSITE)

cleanDir:
	@rm -rf .settings .project *.xml .apt_generated .classpath output .toolkitList impl

