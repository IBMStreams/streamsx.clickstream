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
            build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o \
            build/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.o \
            build/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.o \
            build/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.o \
            build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o \
            build/type/BeJyrNI83NIkEAl9fF5eMjNzc4mJDSxA_13tc33sUlPiMjPjc3HiQI4YOlEIJAEaA4iqCRMRbtQDLXyBiLERAJLMaAJADJ9TeQ.o 
SPL_FUNCTIONS = 
SPL_OPERATORS = build/operator/ThrottleClkStm.o \
                build/operator/ClkStrmEnriched.o \
                build/operator/FileSinkClkStrm.o \
                build/operator/RunGatedClkStrm/outputStream.o 
SPL_SO_BINS = bin/ThrottleClkStm.so \
              bin/ClkStrmEnriched.so \
              bin/FileSinkClkStrm.so \
              bin/RunGatedClkStrm.outputStream.so 

SPL_ADL_FILE = com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.adl

SPL_OUTPUT_DIR_ROOT = $(shell printf '%q' '/mnt/hgfs/StreamsDockerWorkspace/streamsx.clickstream/sample/002_Clickstream_Enrich/output/com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich')
SPL_OUTPUT_DIR = $(shell printf '%q' 'BuildConfig')

.PHONY: distclean clean all types functions operators sos bundle toolkits standalone sablink

all: bin types functions operators sos standalone bundle sablink

distclean clean:
	@rm -fr bin/* build/type build/function build/operator build/bundle build/standalone com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.sab

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

build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o: \
	    src/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.h \
	    src/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] enum{WindowMarker,FinalMarker}'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.cpp

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

build/type/BeJyrNI83NIkEAl9fF5eMjNzc4mJDSxA_13tc33sUlPiMjPjc3HiQI4YOlEIJAEaA4iqCRMRbtQDLXyBiLERAJLMaAJADJ9TeQ.o: \
	    src/type/BeJyrNI83NIkEAl9fF5eMjNzc4mJDSxA_13tc33sUlPiMjPjc3HiQI4YOlEIJAEaA4iqCRMRbtQDLXyBiLERAJLMaAJADJ9TeQ.h \
	    src/type/BeJyrNI83NIkEAl9fF5eMjNzc4mJDSxA_13tc33sUlPiMjPjc3HiQI4YOlEIJAEaA4iqCRMRbtQDLXyBiLERAJLMaAJADJ9TeQ.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] enum{YYYYMMDDhhmmss,YYYY_MM_DD_hh_mm_ss,MM_DD_YYYY_hh_mm_...M_YYYY_hh_mm_ss_mmm}'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJyrNI83NIkEAl9fF5eMjNzc4mJDSxA_13tc33sUlPiMjPjc3HiQI4YOlEIJAEaA4iqCRMRbtQDLXyBiLERAJLMaAJADJ9TeQ.cpp

build/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.o: \
	    src/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.h \
	    src/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<int64 customer_id,rstring time_stamp,rstring click_...oat64 product_price>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.cpp

build/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.o: \
	    src/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.h \
	    src/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<int64 customer_id,rstring time_stamp,rstring click_...p,int64 wcTimestamp>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.cpp

build/type:
	-@mkdir -m 755 build/type

operators: $(SPL_OPERATORS)

-include build/operator/ThrottleClkStm.d
build/operator/ThrottleClkStm.o: \
	    src/operator/ThrottleClkStm.h \
	    src/operator/ThrottleClkStm.cpp\
	    build/dep/operator/ThrottleClkStm.dep  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] ThrottleClkStm'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.adl\" -c $(SPL_CXXFLAGS) src/operator/ThrottleClkStm.cpp

-include build/operator/ClkStrmEnriched.d
build/operator/ClkStrmEnriched.o: \
	    src/operator/ClkStrmEnriched.h \
	    src/operator/ClkStrmEnriched.cpp\
	    build/dep/operator/ClkStrmEnriched.dep \
	    src/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.h \
	    src/type/BeJyrNI83NIkEAl9fF5eMjNzc4mJDSxA_13tc33sUlPiMjPjc3HiQI4YOlEIJAEaA4iqCRMRbtQDLXyBiLERAJLMaAJADJ9TeQ.h  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] ClkStrmEnriched'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.adl\" -c $(SPL_CXXFLAGS) src/operator/ClkStrmEnriched.cpp

-include build/operator/FileSinkClkStrm.d
build/operator/FileSinkClkStrm.o: \
	    src/operator/FileSinkClkStrm.h \
	    src/operator/FileSinkClkStrm.cpp\
	    build/dep/operator/FileSinkClkStrm.dep \
	    src/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.h \
	    src/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.h \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.h  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] FileSinkClkStrm'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.adl\" -c $(SPL_CXXFLAGS) src/operator/FileSinkClkStrm.cpp

-include build/operator/RunGatedClkStrm/outputStream.d
build/operator/RunGatedClkStrm/outputStream.o: \
	    src/operator/RunGatedClkStrm/outputStream.h \
	    src/operator/RunGatedClkStrm/outputStream.cpp\
	    build/dep/operator/RunGatedClkStrm/outputStream.dep \
	    src/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.h  \
	    build/cppOptions \
	    | build/operator/RunGatedClkStrm
	@echo ' [CXX-operator] RunGatedClkStrm.outputStream'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.adl\" -c $(SPL_CXXFLAGS) src/operator/RunGatedClkStrm/outputStream.cpp

build/operator/RunGatedClkStrm:
	-@mkdir -m 755 -p build/operator/RunGatedClkStrm

build/operator:
	-@mkdir -m 755 -p build/operator

functions: $(SPL_FUNCTIONS)

sos: $(SPL_SO_BINS)

SOThrottleClkStm = \
	    build/operator/ThrottleClkStm.o \
	    build/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.o 

bin/ThrottleClkStm.so: \
	$(SOThrottleClkStm) \
	build/dep/ThrottleClkStm.so \
	build/ldOptions
	@echo ' [LD-so] so ThrottleClkStm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/ThrottleClkStm.so -fPIC -shared $(SOThrottleClkStm) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOClkStrmEnriched = \
	    build/operator/ClkStrmEnriched.o \
	    build/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.o \
	    build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o \
	    build/type/BeJyrNI83NIkEAl9fF5eMjNzc4mJDSxA_13tc33sUlPiMjPjc3HiQI4YOlEIJAEaA4iqCRMRbtQDLXyBiLERAJLMaAJADJ9TeQ.o \
	    build/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.o 

bin/ClkStrmEnriched.so: \
	$(SOClkStrmEnriched) \
	build/dep/ClkStrmEnriched.so \
	build/ldOptions
	@echo ' [LD-so] so ClkStrmEnriched'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/ClkStrmEnriched.so -fPIC -shared $(SOClkStrmEnriched) $(SPL_LDFLAGS)

SOFileSinkClkStrm = \
	    build/operator/FileSinkClkStrm.o \
	    build/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.o \
	    build/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.o \
	    build/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.o \
	    build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o 

bin/FileSinkClkStrm.so: \
	$(SOFileSinkClkStrm) \
	build/dep/FileSinkClkStrm.so \
	build/ldOptions
	@echo ' [LD-so] so FileSinkClkStrm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FileSinkClkStrm.so -fPIC -shared $(SOFileSinkClkStrm) -lstreams-stdtk-runtime -lstreams_boost_iostreams -lstreams_boost_filesystem -lstreams_boost_system $(SPL_LDFLAGS)

SORunGatedClkStrm.outputStream = \
	    build/operator/RunGatedClkStrm/outputStream.o \
	    build/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.o \
	    build/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.o 

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
	@ln -sf standalone bin/com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich
build/standalone:
	-@mkdir -m 755 build/standalone

sablink:

	@ln -sf ../com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.sab bin/sab

bundle: com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.sab

-include build/dep/com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.sab.d
com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.sab: $(SPL_SO_BINS) $(SPL_ADL_FILE) build/dep/com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.sab.d bin/standalone.exe
	@echo ' [Bundle] com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.sab'
	@$(SPL_BUNDLE_BUILDER) $(SPL_OUTPUT_DIR_ROOT) $(SPL_OUTPUT_DIR) $(SPL_ADL_FILE) com.ibm.streamsx.clickstream.enrich.ClkStrmEnrich.sab

