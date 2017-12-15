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

SPL_TYPES = build/type/BeJxdjl0KgzAQhK_1katsjBDzFEpNtWTQ_1ZMeCt2_0Q_0uLjzHwMH2hwzyibP2aisBtKksYajQZoEjb4VI1eYdOwsnwlg3FUcSOhwG9cmwbh8ubF2yqYp3_0f97T0pz4oJBlrvojHcCeiGjQH3FGjsbYS975kn6RrXDF4yKe0w9F0VafID1ctFDF.o \
            build/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.o \
            build/type/BeJxtjVEOwjAMQ69EWjRuwAn4r6osoIh0rZoUabenQwxBxV_1s59gGB4XjlavahROpxVQUnHxJhhPmtljAppYT1cCzKEwojPdAD_0rI1kLs3Ds3ADHfK0vNc0MLS_0y9MO0So9Et1_1UMfrdKZSTwwrrdL0_1lz8tncAQyzDH4n_0ATBERgCL.o \
            build/type/BeJwrMS42NCooyk8pTS6Jz0vMTS02NINxkxNLUtPziyrdDI1hQgVFmcmpAA5dBQ0.o \
            build/type/BeJyFyksKgDAMRdEtGQt1B4KrCCUGKdoPzavg7nWgY4fncuGNvBxRdtZTMxhXVaMBMSkbQqoLkXRDSdo4rkZjbWXtAs4hPaf_1KAG6lXbB_1T8zuS_1VFkWnVzdRWDdX.o 
SPL_FUNCTIONS = 
SPL_OPERATORS = build/operator/ClkStrm.o \
                build/operator/ClkStrmStat.o \
                build/operator/ClkStrmAggregates.o \
                build/operator/PrintLn.o 
SPL_SO_BINS = bin/ClkStrm.so \
              bin/ClkStrmStat.so \
              bin/ClkStrmAggregates.so \
              bin/PrintLn.so 

SPL_ADL_FILE = com.ibm.streamsx.clickstreams.ufc.UFC.adl

SPL_OUTPUT_DIR_ROOT = $(shell printf '%q' '/mnt/hgfs/StreamsDockerWorkspace/streamsx.clickstream/sample/100_Clickstream_Unique_Stats/output/com.ibm.streamsx.clickstreams.ufc.UFC')
SPL_OUTPUT_DIR = $(shell printf '%q' 'BuildConfig')

.PHONY: distclean clean all types functions operators sos bundle toolkits standalone sablink

all: bin types functions operators sos standalone bundle sablink

distclean clean:
	@rm -fr bin/* build/type build/function build/operator build/bundle build/standalone com.ibm.streamsx.clickstreams.ufc.UFC.sab

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

build/type/BeJxdjl0KgzAQhK_1katsjBDzFEpNtWTQ_1ZMeCt2_0Q_0uLjzHwMH2hwzyibP2aisBtKksYajQZoEjb4VI1eYdOwsnwlg3FUcSOhwG9cmwbh8ubF2yqYp3_0f97T0pz4oJBlrvojHcCeiGjQH3FGjsbYS975kn6RrXDF4yKe0w9F0VafID1ctFDF.o: \
	    src/type/BeJxdjl0KgzAQhK_1katsjBDzFEpNtWTQ_1ZMeCt2_0Q_0uLjzHwMH2hwzyibP2aisBtKksYajQZoEjb4VI1eYdOwsnwlg3FUcSOhwG9cmwbh8ubF2yqYp3_0f97T0pz4oJBlrvojHcCeiGjQH3FGjsbYS975kn6RrXDF4yKe0w9F0VafID1ctFDF.h \
	    src/type/BeJxdjl0KgzAQhK_1katsjBDzFEpNtWTQ_1ZMeCt2_0Q_0uLjzHwMH2hwzyibP2aisBtKksYajQZoEjb4VI1eYdOwsnwlg3FUcSOhwG9cmwbh8ubF2yqYp3_0f97T0pz4oJBlrvojHcCeiGjQH3FGjsbYS975kn6RrXDF4yKe0w9F0VafID1ctFDF.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<float64 delay,int64 customer_id,rstring time_stamp,...oat64 product_price>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJxdjl0KgzAQhK_1katsjBDzFEpNtWTQ_1ZMeCt2_0Q_0uLjzHwMH2hwzyibP2aisBtKksYajQZoEjb4VI1eYdOwsnwlg3FUcSOhwG9cmwbh8ubF2yqYp3_0f97T0pz4oJBlrvojHcCeiGjQH3FGjsbYS975kn6RrXDF4yKe0w9F0VafID1ctFDF.cpp

build/type/BeJxtjVEOwjAMQ69EWjRuwAn4r6osoIh0rZoUabenQwxBxV_1s59gGB4XjlavahROpxVQUnHxJhhPmtljAppYT1cCzKEwojPdAD_0rI1kLs3Ds3ADHfK0vNc0MLS_0y9MO0So9Et1_1UMfrdKZSTwwrrdL0_1lz8tncAQyzDH4n_0ATBERgCL.o: \
	    src/type/BeJxtjVEOwjAMQ69EWjRuwAn4r6osoIh0rZoUabenQwxBxV_1s59gGB4XjlavahROpxVQUnHxJhhPmtljAppYT1cCzKEwojPdAD_0rI1kLs3Ds3ADHfK0vNc0MLS_0y9MO0So9Et1_1UMfrdKZSTwwrrdL0_1lz8tncAQyzDH4n_0ATBERgCL.h \
	    src/type/BeJxtjVEOwjAMQ69EWjRuwAn4r6osoIh0rZoUabenQwxBxV_1s59gGB4XjlavahROpxVQUnHxJhhPmtljAppYT1cCzKEwojPdAD_0rI1kLs3Ds3ADHfK0vNc0MLS_0y9MO0So9Et1_1UMfrdKZSTwwrrdL0_1lz8tncAQyzDH4n_0ATBERgCL.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<rstring firstTimestamp,rstring lstTimestamp,int32 c...int32 count_product>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJxtjVEOwjAMQ69EWjRuwAn4r6osoIh0rZoUabenQwxBxV_1s59gGB4XjlavahROpxVQUnHxJhhPmtljAppYT1cCzKEwojPdAD_0rI1kLs3Ds3ADHfK0vNc0MLS_0y9MO0So9Et1_1UMfrdKZSTwwrrdL0_1lz8tncAQyzDH4n_0ATBERgCL.cpp

build/type/BeJwrMS42NCooyk8pTS6Jz0vMTS02NINxkxNLUtPziyrdDI1hQgVFmcmpAA5dBQ0.o: \
	    src/type/BeJwrMS42NCooyk8pTS6Jz0vMTS02NINxkxNLUtPziyrdDI1hQgVFmcmpAA5dBQ0.h \
	    src/type/BeJwrMS42NCooyk8pTS6Jz0vMTS02NINxkxNLUtPziyrdDI1hQgVFmcmpAA5dBQ0.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<rstring product_name,rstring product_category,float64 product_price>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJwrMS42NCooyk8pTS6Jz0vMTS02NINxkxNLUtPziyrdDI1hQgVFmcmpAA5dBQ0.cpp

build/type/BeJyFyksKgDAMRdEtGQt1B4KrCCUGKdoPzavg7nWgY4fncuGNvBxRdtZTMxhXVaMBMSkbQqoLkXRDSdo4rkZjbWXtAs4hPaf_1KAG6lXbB_1T8zuS_1VFkWnVzdRWDdX.o: \
	    src/type/BeJyFyksKgDAMRdEtGQt1B4KrCCUGKdoPzavg7nWgY4fncuGNvBxRdtZTMxhXVaMBMSkbQqoLkXRDSdo4rkZjbWXtAs4hPaf_1KAG6lXbB_1T8zuS_1VFkWnVzdRWDdX.h \
	    src/type/BeJyFyksKgDAMRdEtGQt1B4KrCCUGKdoPzavg7nWgY4fncuGNvBxRdtZTMxhXVaMBMSkbQqoLkXRDSdo4rkZjbWXtAs4hPaf_1KAG6lXbB_1T8zuS_1VFkWnVzdRWDdX.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<rstring click_event_type,rstring time_stamp,int64 c...duct_price> product>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJyFyksKgDAMRdEtGQt1B4KrCCUGKdoPzavg7nWgY4fncuGNvBxRdtZTMxhXVaMBMSkbQqoLkXRDSdo4rkZjbWXtAs4hPaf_1KAG6lXbB_1T8zuS_1VFkWnVzdRWDdX.cpp

build/type:
	-@mkdir -m 755 build/type

operators: $(SPL_OPERATORS)

-include build/operator/ClkStrm.d
build/operator/ClkStrm.o: \
	    src/operator/ClkStrm.h \
	    src/operator/ClkStrm.cpp\
	    build/dep/operator/ClkStrm.dep \
	    src/type/BeJxdjl0KgzAQhK_1katsjBDzFEpNtWTQ_1ZMeCt2_0Q_0uLjzHwMH2hwzyibP2aisBtKksYajQZoEjb4VI1eYdOwsnwlg3FUcSOhwG9cmwbh8ubF2yqYp3_0f97T0pz4oJBlrvojHcCeiGjQH3FGjsbYS975kn6RrXDF4yKe0w9F0VafID1ctFDF.h \
	    src/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.h  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] ClkStrm'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstreams.ufc.UFC.adl\" -c $(SPL_CXXFLAGS) src/operator/ClkStrm.cpp

-include build/operator/ClkStrmStat.d
build/operator/ClkStrmStat.o: \
	    src/operator/ClkStrmStat.h \
	    src/operator/ClkStrmStat.cpp\
	    build/dep/operator/ClkStrmStat.dep \
	    src/type/BeJyFyksKgDAMRdEtGQt1B4KrCCUGKdoPzavg7nWgY4fncuGNvBxRdtZTMxhXVaMBMSkbQqoLkXRDSdo4rkZjbWXtAs4hPaf_1KAG6lXbB_1T8zuS_1VFkWnVzdRWDdX.h \
	    src/type/BeJwrMS42NCooyk8pTS6Jz0vMTS02NINxkxNLUtPziyrdDI1hQgVFmcmpAA5dBQ0.h  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] ClkStrmStat'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstreams.ufc.UFC.adl\" -c $(SPL_CXXFLAGS) src/operator/ClkStrmStat.cpp

-include build/operator/ClkStrmAggregates.d
build/operator/ClkStrmAggregates.o: \
	    src/operator/ClkStrmAggregates.h \
	    src/operator/ClkStrmAggregates.cpp\
	    build/dep/operator/ClkStrmAggregates.dep  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] ClkStrmAggregates'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstreams.ufc.UFC.adl\" -c $(SPL_CXXFLAGS) src/operator/ClkStrmAggregates.cpp

-include build/operator/PrintLn.d
build/operator/PrintLn.o: \
	    src/operator/PrintLn.h \
	    src/operator/PrintLn.cpp\
	    build/dep/operator/PrintLn.dep  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] PrintLn'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/com.ibm.streamsx.json/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstreams.ufc.UFC.adl\" -c $(SPL_CXXFLAGS) src/operator/PrintLn.cpp

build/operator:
	-@mkdir -m 755 -p build/operator

functions: $(SPL_FUNCTIONS)

sos: $(SPL_SO_BINS)

SOClkStrm = \
	    build/operator/ClkStrm.o \
	    build/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.o \
	    build/type/BeJxdjl0KgzAQhK_1katsjBDzFEpNtWTQ_1ZMeCt2_0Q_0uLjzHwMH2hwzyibP2aisBtKksYajQZoEjb4VI1eYdOwsnwlg3FUcSOhwG9cmwbh8ubF2yqYp3_0f97T0pz4oJBlrvojHcCeiGjQH3FGjsbYS975kn6RrXDF4yKe0w9F0VafID1ctFDF.o 

bin/ClkStrm.so: \
	$(SOClkStrm) \
	build/dep/ClkStrm.so \
	build/ldOptions
	@echo ' [LD-so] so ClkStrm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/ClkStrm.so -fPIC -shared $(SOClkStrm) -lstreams-stdtk-runtime -lstreams_boost_iostreams -lstreams_boost_filesystem -lstreams_boost_system $(SPL_LDFLAGS)

SOClkStrmStat = \
	    build/operator/ClkStrmStat.o \
	    build/type/BeJxdjl0KgzAQhK_1katsjBDzFEpNtWTQ_1ZMeCt2_0Q_0uLjzHwMH2hwzyibP2aisBtKksYajQZoEjb4VI1eYdOwsnwlg3FUcSOhwG9cmwbh8ubF2yqYp3_0f97T0pz4oJBlrvojHcCeiGjQH3FGjsbYS975kn6RrXDF4yKe0w9F0VafID1ctFDF.o \
	    build/type/BeJyFyksKgDAMRdEtGQt1B4KrCCUGKdoPzavg7nWgY4fncuGNvBxRdtZTMxhXVaMBMSkbQqoLkXRDSdo4rkZjbWXtAs4hPaf_1KAG6lXbB_1T8zuS_1VFkWnVzdRWDdX.o \
	    build/type/BeJwrMS42NCooyk8pTS6Jz0vMTS02NINxkxNLUtPziyrdDI1hQgVFmcmpAA5dBQ0.o 

bin/ClkStrmStat.so: \
	$(SOClkStrmStat) \
	build/dep/ClkStrmStat.so \
	build/ldOptions
	@echo ' [LD-so] so ClkStrmStat'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/ClkStrmStat.so -fPIC -shared $(SOClkStrmStat) $(SPL_LDFLAGS)

SOClkStrmAggregates = \
	    build/operator/ClkStrmAggregates.o \
	    build/type/BeJyFyksKgDAMRdEtGQt1B4KrCCUGKdoPzavg7nWgY4fncuGNvBxRdtZTMxhXVaMBMSkbQqoLkXRDSdo4rkZjbWXtAs4hPaf_1KAG6lXbB_1T8zuS_1VFkWnVzdRWDdX.o \
	    build/type/BeJxtjVEOwjAMQ69EWjRuwAn4r6osoIh0rZoUabenQwxBxV_1s59gGB4XjlavahROpxVQUnHxJhhPmtljAppYT1cCzKEwojPdAD_0rI1kLs3Ds3ADHfK0vNc0MLS_0y9MO0So9Et1_1UMfrdKZSTwwrrdL0_1lz8tncAQyzDH4n_0ATBERgCL.o \
	    build/type/BeJwrMS42NCooyk8pTS6Jz0vMTS02NINxkxNLUtPziyrdDI1hQgVFmcmpAA5dBQ0.o 

bin/ClkStrmAggregates.so: \
	$(SOClkStrmAggregates) \
	build/dep/ClkStrmAggregates.so \
	build/ldOptions
	@echo ' [LD-so] so ClkStrmAggregates'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/ClkStrmAggregates.so -fPIC -shared $(SOClkStrmAggregates) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOPrintLn = \
	    build/operator/PrintLn.o \
	    build/type/BeJxtjVEOwjAMQ69EWjRuwAn4r6osoIh0rZoUabenQwxBxV_1s59gGB4XjlavahROpxVQUnHxJhhPmtljAppYT1cCzKEwojPdAD_0rI1kLs3Ds3ADHfK0vNc0MLS_0y9MO0So9Et1_1UMfrdKZSTwwrrdL0_1lz8tncAQyzDH4n_0ATBERgCL.o \
	    build/type/BeJwrMS42NCooyk8pTS6Jz0vMTS02NINxkxNLUtPziyrdDI1hQgVFmcmpAA5dBQ0.o 

bin/PrintLn.so: \
	$(SOPrintLn) \
	build/dep/PrintLn.so \
	build/ldOptions
	@echo ' [LD-so] so PrintLn'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/PrintLn.so -fPIC -shared $(SOPrintLn) $(SPL_LDFLAGS)

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
	@ln -sf standalone bin/com.ibm.streamsx.clickstreams.ufc.UFC
build/standalone:
	-@mkdir -m 755 build/standalone

sablink:

	@ln -sf ../com.ibm.streamsx.clickstreams.ufc.UFC.sab bin/sab

bundle: com.ibm.streamsx.clickstreams.ufc.UFC.sab

-include build/dep/com.ibm.streamsx.clickstreams.ufc.UFC.sab.d
com.ibm.streamsx.clickstreams.ufc.UFC.sab: $(SPL_SO_BINS) $(SPL_ADL_FILE) build/dep/com.ibm.streamsx.clickstreams.ufc.UFC.sab.d bin/standalone.exe
	@echo ' [Bundle] com.ibm.streamsx.clickstreams.ufc.UFC.sab'
	@$(SPL_BUNDLE_BUILDER) $(SPL_OUTPUT_DIR_ROOT) $(SPL_OUTPUT_DIR) $(SPL_ADL_FILE) com.ibm.streamsx.clickstreams.ufc.UFC.sab

