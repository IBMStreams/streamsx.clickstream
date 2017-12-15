.PHONY: all distributed clean 

SPLC_FLAGS ?= -a
SPLC = $(STREAMS_INSTALL)/bin/sc
SPL_CMD_ARGS ?= 
SPL_MAIN_COMPOSITE = com.ibm.streamsx.clickstream.ingest::MessageHubIngest

# Toolkit dependencies 
SPLC_TOOLKIT_CLICKSTREAM_DSX_TYPES=../000_Clickstream_DSX_Types
SPLC_TOOLKIT_COM.IBM.STREAMSX.SPL.UTIL=../../com.ibm.streamsx.spl.util
SPLC_TOOLKIT_COM.IBM.STREAMSX.MESSAGEHUB=$(STREAMS_INSTALL)/toolkits/com.ibm.streamsx.messagehub
SPLC_TOOLKIT_COM.IBM.STREAMSX.JSON=$(STREAMS_INSTALL)/toolkits/com.ibm.streamsx.json

# List of all dependencies toolkits 
SPLC_TOOLKITS=$(SPLC_TOOLKIT_CLICKSTREAM_DSX_TYPES):$(SPLC_TOOLKIT_COM.IBM.STREAMSX.SPL.UTIL):$(SPLC_TOOLKIT_COM.IBM.STREAMSX.MESSAGEHUB):$(SPLC_TOOLKIT_COM.IBM.STREAMSX.JSON)

# Add toolkits to the compiler flags
SPLC_FLAGS+= -t $(SPLC_TOOLKITS)

all: distributed

distributed:
	echo $(SPLC_TOOLKITS)
	$(SPLC) $(SPLC_FLAGS) -M $(SPL_MAIN_COMPOSITE) $(SPL_CMD_ARGS)

clean: 
	$(SPLC) $(SPLC_FLAGS) -C -M $(SPL_MAIN_COMPOSITE)

cleanDir:
	@rm -rf .settings .project *.xml .apt_generated .classpath output .toolkitList impl

