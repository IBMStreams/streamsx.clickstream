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
            build/type/BeJwVyEEOgDAIBMA3NUX_101iqe6AkgjH4eullDuOloBofqIIJuvS5QdJbZGhGcMt4V1AsN1g3x36K6xhGn07_0AYMsBpV.o \
            build/type/BeJwrMSw2yUvMTQUADM8CDu.o \
            build/type/BeJxdjksKwzAMRK8UJaXQCwSy7144jlpE4g_1WuJDb15R6k_0XMPIaHx0LkqyEFKazbkwZoEDa4kI3u_1lC_1s3wkgnFmmUdCgjs4F_1XC6cWrs12wTP8_01rC2pzYoJBhr7MRtuBKbGjR6XFGjMZe01bZEF6Rp9Ogd5J3KOdPUq5_1IFx4VE30.o \
            build/type/BeJyrNIo3SUksSTXJS8xNBQAf2wSy.o \
            build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o \
            build/type/BeJyrNIq3TCxOTs1LycxLNzRISYWxAXcRAll.o 
SPL_FUNCTIONS = 
SPL_OPERATORS = build/operator/DirScanData.o \
                build/operator/PrintLn.o \
                build/operator/TupleClkStrm.o \
                build/operator/TupleDSXClkStrm.o \
                build/operator/ThrottledDSXClkStrm.o 
SPL_SO_BINS = bin/DirScanData.so \
              bin/PrintLn.so \
              bin/TupleClkStrm.so \
              bin/TupleDSXClkStrm.so \
              bin/ThrottledDSXClkStrm.so 

SPL_ADL_FILE = com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.adl

SPL_OUTPUT_DIR_ROOT = $(shell printf '%q' '/mnt/hgfs/StreamsDockerWorkspace/streamsx.clickstream/sample/101_Clickstream_DSX_Data_Ingest/output/com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest')
SPL_OUTPUT_DIR = $(shell printf '%q' 'BuildConfig')

.PHONY: distclean clean all types functions operators sos bundle toolkits standalone sablink

all: bin types functions operators sos standalone bundle sablink

distclean clean:
	@rm -fr bin/* build/type build/function build/operator build/bundle build/standalone com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.sab

bin:
	@mkdir -m 755 bin

types: $(SPL_TYPES)

build/type/BeJyrNIo3SUksSTXJS8xNBQAf2wSy.o: \
	    src/type/BeJyrNIo3SUksSTXJS8xNBQAf2wSy.h \
	    src/type/BeJyrNIo3SUksSTXJS8xNBQAf2wSy.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] enum{date,name}'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJyrNIo3SUksSTXJS8xNBQAf2wSy.cpp

build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o: \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.h \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] enum{csv,txt,bin,block,line}'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.cpp

build/type/BeJyrNIq3TCxOTs1LycxLNzRISYWxAXcRAll.o: \
	    src/type/BeJyrNIq3TCxOTs1LycxLNzRISYWxAXcRAll.h \
	    src/type/BeJyrNIq3TCxOTs1LycxLNzRISYWxAXcRAll.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] enum{ascending,descending}'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJyrNIq3TCxOTs1LycxLNzRISYWxAXcRAll.cpp

build/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.o: \
	    src/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.h \
	    src/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<int64 customer_id,rstring time_stamp,rstring click_...oat64 product_price>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.cpp

build/type/BeJwVyEEOgDAIBMA3NUX_101iqe6AkgjH4eullDuOloBofqIIJuvS5QdJbZGhGcMt4V1AsN1g3x36K6xhGn07_0AYMsBpV.o: \
	    src/type/BeJwVyEEOgDAIBMA3NUX_101iqe6AkgjH4eullDuOloBofqIIJuvS5QdJbZGhGcMt4V1AsN1g3x36K6xhGn07_0AYMsBpV.h \
	    src/type/BeJwVyEEOgDAIBMA3NUX_101iqe6AkgjH4eullDuOloBofqIIJuvS5QdJbZGhGcMt4V1AsN1g3x36K6xhGn07_0AYMsBpV.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<int32 sec,int32 min,int32 hour,int32 mday,int32 mon...gmtoff,rstring zone>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJwVyEEOgDAIBMA3NUX_101iqe6AkgjH4eullDuOloBofqIIJuvS5QdJbZGhGcMt4V1AsN1g3x36K6xhGn07_0AYMsBpV.cpp

build/type/BeJwrMSw2yUvMTQUADM8CDu.o: \
	    src/type/BeJwrMSw2yUvMTQUADM8CDu.h \
	    src/type/BeJwrMSw2yUvMTQUADM8CDu.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<rstring name>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJwrMSw2yUvMTQUADM8CDu.cpp

build/type/BeJxdjksKwzAMRK8UJaXQCwSy7144jlpE4g_1WuJDb15R6k_0XMPIaHx0LkqyEFKazbkwZoEDa4kI3u_1lC_1s3wkgnFmmUdCgjs4F_1XC6cWrs12wTP8_01rC2pzYoJBhr7MRtuBKbGjR6XFGjMZe01bZEF6Rp9Ogd5J3KOdPUq5_1IFx4VE30.o: \
	    src/type/BeJxdjksKwzAMRK8UJaXQCwSy7144jlpE4g_1WuJDb15R6k_0XMPIaHx0LkqyEFKazbkwZoEDa4kI3u_1lC_1s3wkgnFmmUdCgjs4F_1XC6cWrs12wTP8_01rC2pzYoJBhr7MRtuBKbGjR6XFGjMZe01bZEF6Rp9Ogd5J3KOdPUq5_1IFx4VE30.h \
	    src/type/BeJxdjksKwzAMRK8UJaXQCwSy7144jlpE4g_1WuJDb15R6k_0XMPIaHx0LkqyEFKazbkwZoEDa4kI3u_1lC_1s3wkgnFmmUdCgjs4F_1XC6cWrs12wTP8_01rC2pzYoJBhr7MRtuBKbGjR6XFGjMZe01bZEF6Rp9Ogd5J3KOdPUq5_1IFx4VE30.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<int64 customer_id,timestamp time_stamp,rstring clic...oat64 product_price>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJxdjksKwzAMRK8UJaXQCwSy7144jlpE4g_1WuJDb15R6k_0XMPIaHx0LkqyEFKazbkwZoEDa4kI3u_1lC_1s3wkgnFmmUdCgjs4F_1XC6cWrs12wTP8_01rC2pzYoJBhr7MRtuBKbGjR6XFGjMZe01bZEF6Rp9Ogd5J3KOdPUq5_1IFx4VE30.cpp

build/type:
	-@mkdir -m 755 build/type

operators: $(SPL_OPERATORS)

-include build/operator/DirScanData.d
build/operator/DirScanData.o: \
	    src/operator/DirScanData.h \
	    src/operator/DirScanData.cpp\
	    build/dep/operator/DirScanData.dep \
	    src/type/BeJyrNIq3TCxOTs1LycxLNzRISYWxAXcRAll.h \
	    src/type/BeJyrNIo3SUksSTXJS8xNBQAf2wSy.h  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] DirScanData'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/DirScanData.cpp

-include build/operator/PrintLn.d
build/operator/PrintLn.o: \
	    src/operator/PrintLn.h \
	    src/operator/PrintLn.cpp\
	    build/dep/operator/PrintLn.dep  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] PrintLn'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/PrintLn.cpp

-include build/operator/TupleClkStrm.d
build/operator/TupleClkStrm.o: \
	    src/operator/TupleClkStrm.h \
	    src/operator/TupleClkStrm.cpp\
	    build/dep/operator/TupleClkStrm.dep \
	    src/type/BeJwrMSw2yUvMTQUADM8CDu.h \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.h  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] TupleClkStrm'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/TupleClkStrm.cpp

-include build/operator/TupleDSXClkStrm.d
build/operator/TupleDSXClkStrm.o: \
	    src/operator/TupleDSXClkStrm.h \
	    src/operator/TupleDSXClkStrm.cpp\
	    build/dep/operator/TupleDSXClkStrm.dep \
	    src/type/BeJwVyEEOgDAIBMA3NUX_101iqe6AkgjH4eullDuOloBofqIIJuvS5QdJbZGhGcMt4V1AsN1g3x36K6xhGn07_0AYMsBpV.h  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] TupleDSXClkStrm'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/TupleDSXClkStrm.cpp

-include build/operator/ThrottledDSXClkStrm.d
build/operator/ThrottledDSXClkStrm.o: \
	    src/operator/ThrottledDSXClkStrm.h \
	    src/operator/ThrottledDSXClkStrm.cpp\
	    build/dep/operator/ThrottledDSXClkStrm.dep  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] ThrottledDSXClkStrm'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.adl\" -c $(SPL_CXXFLAGS) src/operator/ThrottledDSXClkStrm.cpp

build/operator:
	-@mkdir -m 755 -p build/operator

functions: $(SPL_FUNCTIONS)

sos: $(SPL_SO_BINS)

SODirScanData = \
	    build/operator/DirScanData.o \
	    build/type/BeJwrMSw2yUvMTQUADM8CDu.o \
	    build/type/BeJyrNIq3TCxOTs1LycxLNzRISYWxAXcRAll.o \
	    build/type/BeJyrNIo3SUksSTXJS8xNBQAf2wSy.o 

bin/DirScanData.so: \
	$(SODirScanData) \
	build/dep/DirScanData.so \
	build/ldOptions
	@echo ' [LD-so] so DirScanData'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/DirScanData.so -fPIC -shared $(SODirScanData) -lstreams-stdtk-runtime -lstreams_boost_filesystem -lstreams_boost_system $(SPL_LDFLAGS)

SOPrintLn = \
	    build/operator/PrintLn.o \
	    build/type/BeJwrMSw2yUvMTQUADM8CDu.o 

bin/PrintLn.so: \
	$(SOPrintLn) \
	build/dep/PrintLn.so \
	build/ldOptions
	@echo ' [LD-so] so PrintLn'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/PrintLn.so -fPIC -shared $(SOPrintLn) $(SPL_LDFLAGS)

SOTupleClkStrm = \
	    build/operator/TupleClkStrm.o \
	    build/type/BeJwrMSw2yUvMTQUADM8CDu.o \
	    build/type/BeJxdjksKwzAMRK8UJaXQCwSy7144jlpE4g_1WuJDb15R6k_0XMPIaHx0LkqyEFKazbkwZoEDa4kI3u_1lC_1s3wkgnFmmUdCgjs4F_1XC6cWrs12wTP8_01rC2pzYoJBhr7MRtuBKbGjR6XFGjMZe01bZEF6Rp9Ogd5J3KOdPUq5_1IFx4VE30.o \
	    build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o 

bin/TupleClkStrm.so: \
	$(SOTupleClkStrm) \
	build/dep/TupleClkStrm.so \
	build/ldOptions
	@echo ' [LD-so] so TupleClkStrm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/TupleClkStrm.so -fPIC -shared $(SOTupleClkStrm) -lstreams-stdtk-runtime -lstreams_boost_iostreams -lstreams_boost_filesystem -lstreams_boost_system $(SPL_LDFLAGS)

SOTupleDSXClkStrm = \
	    build/operator/TupleDSXClkStrm.o \
	    build/type/BeJxdjksKwzAMRK8UJaXQCwSy7144jlpE4g_1WuJDb15R6k_0XMPIaHx0LkqyEFKazbkwZoEDa4kI3u_1lC_1s3wkgnFmmUdCgjs4F_1XC6cWrs12wTP8_01rC2pzYoJBhr7MRtuBKbGjR6XFGjMZe01bZEF6Rp9Ogd5J3KOdPUq5_1IFx4VE30.o \
	    build/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.o \
	    build/type/BeJwVyEEOgDAIBMA3NUX_101iqe6AkgjH4eullDuOloBofqIIJuvS5QdJbZGhGcMt4V1AsN1g3x36K6xhGn07_0AYMsBpV.o 

bin/TupleDSXClkStrm.so: \
	$(SOTupleDSXClkStrm) \
	build/dep/TupleDSXClkStrm.so \
	build/ldOptions
	@echo ' [LD-so] so TupleDSXClkStrm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/TupleDSXClkStrm.so -fPIC -shared $(SOTupleDSXClkStrm) $(SPL_LDFLAGS)

SOThrottledDSXClkStrm = \
	    build/operator/ThrottledDSXClkStrm.o \
	    build/type/BeJxdjl0KgzAQhK_1kain0AoKnWGKyLYvmh_0yk4O0bpL74ODMfw4fXQuSbIUeprMFogEZhg4vF6Ol39RvLVxIYR5F5JGS4nUtVL5zfvDrbBMv071OLa3_1qg0KisaaLeAx3IqhBk8cdNRpLzaH1JbkoXeOK3kE_0uR4zTVd1ivwAND5OAT.o 

bin/ThrottledDSXClkStrm.so: \
	$(SOThrottledDSXClkStrm) \
	build/dep/ThrottledDSXClkStrm.so \
	build/ldOptions
	@echo ' [LD-so] so ThrottledDSXClkStrm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/ThrottledDSXClkStrm.so -fPIC -shared $(SOThrottledDSXClkStrm) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

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
	@ln -sf standalone bin/com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest
build/standalone:
	-@mkdir -m 755 build/standalone

sablink:

	@ln -sf ../com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.sab bin/sab

bundle: com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.sab

-include build/dep/com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.sab.d
com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.sab: $(SPL_SO_BINS) $(SPL_ADL_FILE) build/dep/com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.sab.d bin/standalone.exe
	@echo ' [Bundle] com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.sab'
	@$(SPL_BUNDLE_BUILDER) $(SPL_OUTPUT_DIR_ROOT) $(SPL_OUTPUT_DIR) $(SPL_ADL_FILE) com.ibm.streamsx.clickstream.ingest.DSXOfflineIngest.sab

