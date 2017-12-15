# NOTE: This makefile is designed to be run from one level up in the directory
# hierarchy compared to where it resides. For instance, if this makefile is
# located at 'output/build/Makefile', then it can be launched as:
# 'make -f build/Makefile' from the 'output' directory.

SHELL=/bin/bash
ifeq ($(CXX),)
  CXX=g++
endif
PKGCONFIG := /opt/ibm/InfoSphere_Streams/4.2.1.1/bin/dst-pe-pkg-config.sh
SPL_BUNDLE_BUILDER := /opt/ibm/InfoSphere_Streams/4.2.1.1/system/impl/bin/spl-bundle-builder
SO_INCLUDE := $(shell $(PKGCONFIG) --cflags dst-spl-pe-install)
SO_LIB := $(shell $(PKGCONFIG) --libs dst-spl-pe-install)
SO_STAND_LIB := $(shell $(PKGCONFIG) --libs dst-spl-pe-install-standalone)
SPL_CXXFLAGS = -Wall -Wno-unused -Wno-sign-compare
SPL_CXXFLAGS += -D_REENTRANT -fPIC -finline-functions -fmessage-length=0
SPL_CXXFLAGS += $(SO_INCLUDE) -O3 -DNDEBUG  -std=gnu++98 
SPL_LDFLAGS = $(SO_LIB)

SPL_TYPES = build/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.o \
            build/type/BeJwrMSw2yUvMTQUADM8CDu.o \
            build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o \
            build/type/BeJxdjl0Kg0AQg6_1kaBF6gYKnGNbdaRl0f9iJBW_1fteiLj0m_0hOBpNPpV_1cLylQTGXsSog0Zhg4tlGggZbuW0xVkq5zcrJBpr4tnZIpge3Z0IatDkcUdf_1TlWqno5yNOnodQcttb4JxOR3ww5tjkNRv2VJhfbvfGS3kE_0ue4_1ZuJOAT.o 
SPL_FUNCTIONS = 
SPL_OPERATORS = build/operator/DirScanData.o \
                build/operator/TupleClkStrm.o 
SPL_SO_BINS = bin/DirScanData.so \
              bin/TupleClkStrm.so 

SPL_ADL_FILE = com.ibm.streamsx.clickstream.ingest.OfflineIngest.adl

SPL_OUTPUT_DIR_ROOT = $(shell printf '%q' '/mnt/hgfs/StreamsDockerWorkspace/streamsx.clickstream/sample/001_Clickstream_Offline_Ingest')
SPL_OUTPUT_DIR = $(shell printf '%q' 'output')

.PHONY: distclean clean all types functions operators sos bundle toolkits standalone sablink

all: bin types functions operators sos standalone bundle sablink

distclean clean:
	@rm -fr bin/* build/type build/function build/operator build/bundle build/standalone com.ibm.streamsx.clickstream.ingest.OfflineIngest.sab

bin:
	@mkdir -m 755 bin

types: $(SPL_TYPES)

build/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.o: \
	    src/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.h \
	    src/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] enum{zlib,gzip,bzip2}'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.cpp

build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o: \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.h \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] enum{csv,txt,bin,block,line}'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.cpp

build/type/BeJwrMSw2yUvMTQUADM8CDu.o: \
	    src/type/BeJwrMSw2yUvMTQUADM8CDu.h \
	    src/type/BeJwrMSw2yUvMTQUADM8CDu.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<rstring name>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJwrMSw2yUvMTQUADM8CDu.cpp

build/type/BeJxdjl0Kg0AQg6_1kaBF6gYKnGNbdaRl0f9iJBW_1fteiLj0m_0hOBpNPpV_1cLylQTGXsSog0Zhg4tlGggZbuW0xVkq5zcrJBpr4tnZIpge3Z0IatDkcUdf_1TlWqno5yNOnodQcttb4JxOR3ww5tjkNRv2VJhfbvfGS3kE_0ue4_1ZuJOAT.o: \
	    src/type/BeJxdjl0Kg0AQg6_1kaBF6gYKnGNbdaRl0f9iJBW_1fteiLj0m_0hOBpNPpV_1cLylQTGXsSog0Zhg4tlGggZbuW0xVkq5zcrJBpr4tnZIpge3Z0IatDkcUdf_1TlWqno5yNOnodQcttb4JxOR3ww5tjkNRv2VJhfbvfGS3kE_0ue4_1ZuJOAT.h \
	    src/type/BeJxdjl0Kg0AQg6_1kaBF6gYKnGNbdaRl0f9iJBW_1fteiLj0m_0hOBpNPpV_1cLylQTGXsSog0Zhg4tlGggZbuW0xVkq5zcrJBpr4tnZIpge3Z0IatDkcUdf_1TlWqno5yNOnodQcttb4JxOR3ww5tjkNRv2VJhfbvfGS3kE_0ue4_1ZuJOAT.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<rstring click_event_type,rstring time_stamp,int64 t...ng product_category>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJxdjl0Kg0AQg6_1kaBF6gYKnGNbdaRl0f9iJBW_1fteiLj0m_0hOBpNPpV_1cLylQTGXsSog0Zhg4tlGggZbuW0xVkq5zcrJBpr4tnZIpge3Z0IatDkcUdf_1TlWqno5yNOnodQcttb4JxOR3ww5tjkNRv2VJhfbvfGS3kE_0ue4_1ZuJOAT.cpp

build/type:
	-@mkdir -m 755 build/type

operators: $(SPL_OPERATORS)

-include build/operator/DirScanData.d
build/operator/DirScanData.o: \
	    src/operator/DirScanData.h \
	    src/operator/DirScanData.cpp\
	    build/dep/operator/DirScanData.dep  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] DirScanData'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.OfflineIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/DirScanData.cpp

-include build/operator/TupleClkStrm.d
build/operator/TupleClkStrm.o: \
	    src/operator/TupleClkStrm.h \
	    src/operator/TupleClkStrm.cpp\
	    build/dep/operator/TupleClkStrm.dep \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.h \
	    src/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.h  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] TupleClkStrm'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.OfflineIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/TupleClkStrm.cpp

build/operator:
	-@mkdir -m 755 -p build/operator

functions: $(SPL_FUNCTIONS)

sos: $(SPL_SO_BINS)

SODirScanData = \
	    build/operator/DirScanData.o \
	    build/type/BeJwrMSw2yUvMTQUADM8CDu.o 

bin/DirScanData.so: \
	$(SODirScanData) \
	build/dep/DirScanData.so \
	build/ldOptions
	@echo ' [LD-so] so DirScanData'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/DirScanData.so -fPIC -shared $(SODirScanData) -lstreams-stdtk-runtime -lstreams_boost_filesystem -lstreams_boost_system $(SPL_LDFLAGS)

SOTupleClkStrm = \
	    build/operator/TupleClkStrm.o \
	    build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o \
	    build/type/BeJxdjl0Kg0AQg6_1kaBF6gYKnGNbdaRl0f9iJBW_1fteiLj0m_0hOBpNPpV_1cLylQTGXsSog0Zhg4tlGggZbuW0xVkq5zcrJBpr4tnZIpge3Z0IatDkcUdf_1TlWqno5yNOnodQcttb4JxOR3ww5tjkNRv2VJhfbvfGS3kE_0ue4_1ZuJOAT.o \
	    build/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.o \
	    build/type/BeJwrMSw2yUvMTQUADM8CDu.o 

bin/TupleClkStrm.so: \
	$(SOTupleClkStrm) \
	build/dep/TupleClkStrm.so \
	build/ldOptions
	@echo ' [LD-so] so TupleClkStrm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/TupleClkStrm.so -fPIC -shared $(SOTupleClkStrm) -lstreams-stdtk-runtime -lstreams_boost_iostreams -lstreams_boost_filesystem -lstreams_boost_system $(SPL_LDFLAGS)

standalone: bin/standalone.exe

build/standalone/standalone.o: \
	    src/standalone/standalone.h \
	    src/standalone/standalone.cpp  \
	    build/cppOptions \
	    | build/standalone
	@echo ' [CXX-standalone] standalone'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/standalone/standalone.cpp

bin/standalone.exe: build/standalone/standalone.o build/ldOptions
	@echo ' [LD-standalone] standalone'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/standalone.exe build/standalone/standalone.o $(SO_STAND_LIB)
	@echo ' [LN-standalone] standalone '
	@ln -sf standalone bin/com.ibm.streamsx.clickstream.ingest.OfflineIngest
build/standalone:
	-@mkdir -m 755 build/standalone

sablink:

	@ln -sf ../com.ibm.streamsx.clickstream.ingest.OfflineIngest.sab bin/sab

bundle: com.ibm.streamsx.clickstream.ingest.OfflineIngest.sab

-include build/dep/com.ibm.streamsx.clickstream.ingest.OfflineIngest.sab.d
com.ibm.streamsx.clickstream.ingest.OfflineIngest.sab: $(SPL_SO_BINS) $(SPL_ADL_FILE) build/dep/com.ibm.streamsx.clickstream.ingest.OfflineIngest.sab.d bin/standalone.exe
	@echo ' [Bundle] com.ibm.streamsx.clickstream.ingest.OfflineIngest.sab'
	@$(SPL_BUNDLE_BUILDER) $(SPL_OUTPUT_DIR_ROOT) $(SPL_OUTPUT_DIR) $(SPL_ADL_FILE) com.ibm.streamsx.clickstream.ingest.OfflineIngest.sab

