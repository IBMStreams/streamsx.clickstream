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

SPL_TYPES = build/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.o \
            build/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.o \
            build/type/BeJwrMSw2z00tLk5MTwUAGG4EA1.o \
            build/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.o \
            build/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.o \
            build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o 
SPL_FUNCTIONS = 
SPL_OPERATORS = build/operator/MessageHubClkStrm.o \
                build/operator/ThrottleClkStm.o \
                build/operator/TupleClkStrm.o \
                build/operator/FileSinkClkStrm.o \
                build/operator/RunGatedClkStrm/outputStream.o 
SPL_SO_BINS = bin/MessageHubClkStrm.so \
              bin/ThrottleClkStm.so \
              bin/TupleClkStrm.so \
              bin/FileSinkClkStrm.so \
              bin/RunGatedClkStrm.outputStream.so 

SPL_ADL_FILE = com.ibm.streamsx.clickstream.ingest.MessageHubIngest.adl

SPL_OUTPUT_DIR_ROOT = $(shell printf '%q' '/mnt/hgfs/StreamsDockerWorkspace/streamsx.clickstream/sample/001_Clickstream_MessageHub_Ingest/output/com.ibm.streamsx.clickstream.ingest.MessageHubIngest')
SPL_OUTPUT_DIR = $(shell printf '%q' 'BuildConfig')

.PHONY: distclean clean all types functions operators sos bundle toolkits standalone sablink

all: bin types functions operators sos standalone bundle sablink

distclean clean:
	@rm -fr bin/* build/type build/function build/operator build/bundle build/standalone com.ibm.streamsx.clickstream.ingest.MessageHubIngest.sab

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

build/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.o: \
	    src/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.h \
	    src/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] enum{punct,count,size,time,dynamic,never}'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.cpp

build/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.o: \
	    src/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.h \
	    src/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] enum{error,warn,info,debug,trace}'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.cpp

build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o: \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.h \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] enum{csv,txt,bin,block,line}'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.cpp

build/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.o: \
	    src/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.h \
	    src/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<int64 customer_id,rstring time_stamp,rstring click_...oat64 product_price>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.cpp

build/type/BeJwrMSw2z00tLk5MTwUAGG4EA1.o: \
	    src/type/BeJwrMSw2z00tLk5MTwUAGG4EA1.h \
	    src/type/BeJwrMSw2z00tLk5MTwUAGG4EA1.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<rstring message>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJwrMSw2z00tLk5MTwUAGG4EA1.cpp

build/type:
	-@mkdir -m 755 build/type

operators: $(SPL_OPERATORS)

-include build/operator/MessageHubClkStrm.d
build/operator/MessageHubClkStrm.o: \
	    src/operator/MessageHubClkStrm.h \
	    src/operator/MessageHubClkStrm.cpp\
	    build/dep/operator/MessageHubClkStrm.dep  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] MessageHubClkStrm'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/com.ibm.streamsx.messagehub/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/spl/utility/JavaOp/../../../impl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/java/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.MessageHubIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/MessageHubClkStrm.cpp

-include build/operator/ThrottleClkStm.d
build/operator/ThrottleClkStm.o: \
	    src/operator/ThrottleClkStm.h \
	    src/operator/ThrottleClkStm.cpp\
	    build/dep/operator/ThrottleClkStm.dep  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] ThrottleClkStm'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.MessageHubIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/ThrottleClkStm.cpp

-include build/operator/TupleClkStrm.d
build/operator/TupleClkStrm.o: \
	    src/operator/TupleClkStrm.h \
	    src/operator/TupleClkStrm.cpp\
	    build/dep/operator/TupleClkStrm.dep  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] TupleClkStrm'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/com.ibm.streamsx.json/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/spl/utility/JavaOp/../../../impl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/java/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.MessageHubIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/TupleClkStrm.cpp

-include build/operator/FileSinkClkStrm.d
build/operator/FileSinkClkStrm.o: \
	    src/operator/FileSinkClkStrm.h \
	    src/operator/FileSinkClkStrm.cpp\
	    build/dep/operator/FileSinkClkStrm.dep \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.h \
	    src/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.h \
	    src/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.h \
	    src/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.h  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] FileSinkClkStrm'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.MessageHubIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/FileSinkClkStrm.cpp

-include build/operator/RunGatedClkStrm/outputStream.d
build/operator/RunGatedClkStrm/outputStream.o: \
	    src/operator/RunGatedClkStrm/outputStream.h \
	    src/operator/RunGatedClkStrm/outputStream.cpp\
	    build/dep/operator/RunGatedClkStrm/outputStream.dep \
	    src/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.h  \
	    build/cppOptions \
	    | build/operator/RunGatedClkStrm
	@echo ' [CXX-operator] RunGatedClkStrm.outputStream'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.MessageHubIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/RunGatedClkStrm/outputStream.cpp

build/operator/RunGatedClkStrm:
	-@mkdir -m 755 -p build/operator/RunGatedClkStrm

build/operator:
	-@mkdir -m 755 -p build/operator

functions: $(SPL_FUNCTIONS)

sos: $(SPL_SO_BINS)

SOMessageHubClkStrm = \
	    build/operator/MessageHubClkStrm.o \
	    build/type/BeJwrMSw2z00tLk5MTwUAGG4EA1.o 

bin/MessageHubClkStrm.so: \
	$(SOMessageHubClkStrm) \
	build/dep/MessageHubClkStrm.so \
	build/ldOptions
	@echo ' [LD-so] so MessageHubClkStrm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/MessageHubClkStrm.so -fPIC -shared $(SOMessageHubClkStrm) -lstreams-stdtk-javaop -L /opt/ibm/InfoSphere_Streams/4.2.1.1/java/jre/lib/amd64/j9vm -Wl,-rpath -Wl,/opt/ibm/InfoSphere_Streams/4.2.1.1/java/jre/lib/amd64/j9vm -lpthread -ldl -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOThrottleClkStm = \
	    build/operator/ThrottleClkStm.o \
	    build/type/BeJwrMSw2z00tLk5MTwUAGG4EA1.o 

bin/ThrottleClkStm.so: \
	$(SOThrottleClkStm) \
	build/dep/ThrottleClkStm.so \
	build/ldOptions
	@echo ' [LD-so] so ThrottleClkStm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/ThrottleClkStm.so -fPIC -shared $(SOThrottleClkStm) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOTupleClkStrm = \
	    build/operator/TupleClkStrm.o \
	    build/type/BeJwrMSw2z00tLk5MTwUAGG4EA1.o \
	    build/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.o 

bin/TupleClkStrm.so: \
	$(SOTupleClkStrm) \
	build/dep/TupleClkStrm.so \
	build/ldOptions
	@echo ' [LD-so] so TupleClkStrm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/TupleClkStrm.so -fPIC -shared $(SOTupleClkStrm) -lstreams-stdtk-javaop -L /opt/ibm/InfoSphere_Streams/4.2.1.1/java/jre/lib/amd64/j9vm -Wl,-rpath -Wl,/opt/ibm/InfoSphere_Streams/4.2.1.1/java/jre/lib/amd64/j9vm -lpthread -ldl -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFileSinkClkStrm = \
	    build/operator/FileSinkClkStrm.o \
	    build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o \
	    build/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.o \
	    build/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.o \
	    build/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.o 

bin/FileSinkClkStrm.so: \
	$(SOFileSinkClkStrm) \
	build/dep/FileSinkClkStrm.so \
	build/ldOptions
	@echo ' [LD-so] so FileSinkClkStrm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FileSinkClkStrm.so -fPIC -shared $(SOFileSinkClkStrm) -lstreams-stdtk-runtime -lstreams_boost_iostreams -lstreams_boost_filesystem -lstreams_boost_system $(SPL_LDFLAGS)

SORunGatedClkStrm.outputStream = \
	    build/operator/RunGatedClkStrm/outputStream.o \
	    build/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.o \
	    build/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.o 

bin/RunGatedClkStrm.outputStream.so: \
	$(SORunGatedClkStrm.outputStream) \
	build/dep/RunGatedClkStrm.outputStream.so \
	build/ldOptions
	@echo ' [LD-so] so RunGatedClkStrm.outputStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/RunGatedClkStrm.outputStream.so -fPIC -shared $(SORunGatedClkStrm.outputStream) $(SPL_LDFLAGS)

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
	@ln -sf standalone bin/com.ibm.streamsx.clickstream.ingest.MessageHubIngest
build/standalone:
	-@mkdir -m 755 build/standalone

sablink:

	@ln -sf ../com.ibm.streamsx.clickstream.ingest.MessageHubIngest.sab bin/sab

bundle: com.ibm.streamsx.clickstream.ingest.MessageHubIngest.sab

-include build/dep/com.ibm.streamsx.clickstream.ingest.MessageHubIngest.sab.d
com.ibm.streamsx.clickstream.ingest.MessageHubIngest.sab: $(SPL_SO_BINS) $(SPL_ADL_FILE) build/dep/com.ibm.streamsx.clickstream.ingest.MessageHubIngest.sab.d bin/standalone.exe
	@echo ' [Bundle] com.ibm.streamsx.clickstream.ingest.MessageHubIngest.sab'
	@$(SPL_BUNDLE_BUILDER) $(SPL_OUTPUT_DIR_ROOT) $(SPL_OUTPUT_DIR) $(SPL_ADL_FILE) com.ibm.streamsx.clickstream.ingest.MessageHubIngest.sab

