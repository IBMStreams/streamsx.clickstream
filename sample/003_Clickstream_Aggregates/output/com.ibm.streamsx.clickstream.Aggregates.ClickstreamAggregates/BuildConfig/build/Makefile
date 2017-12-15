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

SPL_TYPES = build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o \
            build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o \
            build/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.o \
            build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o \
            build/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.o \
            build/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.o \
            build/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.o \
            build/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.o \
            build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o 
SPL_FUNCTIONS = build/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.o \
                build/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.o \
                build/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.o \
                build/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.o \
                build/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.o \
                build/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.o \
                build/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.o \
                build/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.o \
                build/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.o 
SPL_OPERATORS = build/operator/ThrottleClkStm.o \
                build/operator/FiveStageCountByDistinctAggregateStream.o \
                build/operator/FileSinkRunGated.o \
                build/operator/FiveStageCountDistinctAggregate.o \
                build/operator/FileSinkRunGatedCountDistinct.o \
                build/operator/FiveStageCountByDistinct/aggOut1/CountByDistinctAggregate.o \
                build/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated/oStream.o \
                build/operator/FiveStageCountByDistinct/aggOut2/CountByDistinctCascadedAggregate.o \
                build/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream/oStream.o \
                build/operator/RunGated/outputStream.o \
                build/operator/FiveStageCountDistinctAggregateAlias/agg1.o \
                build/operator/FiveStageCountDistinctAggregateAlias/aggOut1/CountDistinctAggregate.o \
                build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/CountDistinctCascadedAggregate.o \
                build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream/oStream.o \
                build/operator/RunGatedCountDistinct/outputStream.o 
SPL_SO_BINS = bin/ThrottleClkStm.so \
              bin/FiveStageCountByDistinctAggregateStream.so \
              bin/FileSinkRunGated.so \
              bin/FiveStageCountDistinctAggregate.so \
              bin/FileSinkRunGatedCountDistinct.so \
              bin/FiveStageCountByDistinct.aggOut1.CountByDistinctAggregate.so \
              bin/FiveStageCountByDistinct.aggOut1.ClkStrmPunctuated.oStream.so \
              bin/FiveStageCountByDistinct.aggOut2.CountByDistinctCascadedAggregate.so \
              bin/FiveStageCountByDistinct.aggOut2.PunctuatedAggregatedInputStream.oStream.so \
              bin/RunGated.outputStream.so \
              bin/FiveStageCountDistinctAggregateAlias.agg1.so \
              bin/FiveStageCountDistinctAggregateAlias.aggOut1.CountDistinctAggregate.so \
              bin/FiveStageCountDistinctAggregateAlias.aggOut2.CountDistinctCascadedAggregate.so \
              bin/FiveStageCountDistinctAggregateAlias.aggOut2.PunctuatedAggregatedInputStream.oStream.so \
              bin/RunGatedCountDistinct.outputStream.so 

SPL_ADL_FILE = com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl

SPL_OUTPUT_DIR_ROOT = $(shell printf '%q' '/mnt/hgfs/StreamsDockerWorkspace/streamsx.clickstream/sample/003_Clickstream_Aggregates/output/com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates')
SPL_OUTPUT_DIR = $(shell printf '%q' 'BuildConfig')

.PHONY: distclean clean all types functions operators sos bundle toolkits standalone sablink

all: bin types functions operators sos standalone bundle sablink

distclean clean:
	@rm -fr bin/* build/type build/function build/operator build/bundle build/standalone com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.sab

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

build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o: \
	    src/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.h \
	    src/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<rstring label,rstring groupName,list<rstring> itemC...t64 wcTimestampLast>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.cpp

build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o: \
	    src/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.h \
	    src/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<rstring label,rstring groupName,list<rstring> itemC...t64 wcTimestampLast>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.cpp

build/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.o: \
	    src/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.h \
	    src/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.cpp \
	    build/cppOptions \
	    | build/type
	@echo ' [CXX-type] tuple<rstring label,rstring groupName,int32 itemCountDist...t64 wcTimestampLast>'
	@$(CXX) -o $@ -c $(SPL_CXXFLAGS) src/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.cpp

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
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/ThrottleClkStm.cpp

-include build/operator/FiveStageCountByDistinctAggregateStream.d
build/operator/FiveStageCountByDistinctAggregateStream.o: \
	    src/operator/FiveStageCountByDistinctAggregateStream.h \
	    src/operator/FiveStageCountByDistinctAggregateStream.cpp\
	    build/dep/operator/FiveStageCountByDistinctAggregateStream.dep  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] FiveStageCountByDistinctAggregateStream'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FiveStageCountByDistinctAggregateStream.cpp

-include build/operator/FileSinkRunGated.d
build/operator/FileSinkRunGated.o: \
	    src/operator/FileSinkRunGated.h \
	    src/operator/FileSinkRunGated.cpp\
	    build/dep/operator/FileSinkRunGated.dep \
	    src/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.h \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.h \
	    src/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.h  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] FileSinkRunGated'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FileSinkRunGated.cpp

-include build/operator/FiveStageCountDistinctAggregate.d
build/operator/FiveStageCountDistinctAggregate.o: \
	    src/operator/FiveStageCountDistinctAggregate.h \
	    src/operator/FiveStageCountDistinctAggregate.cpp\
	    build/dep/operator/FiveStageCountDistinctAggregate.dep  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] FiveStageCountDistinctAggregate'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FiveStageCountDistinctAggregate.cpp

-include build/operator/FileSinkRunGatedCountDistinct.d
build/operator/FileSinkRunGatedCountDistinct.o: \
	    src/operator/FileSinkRunGatedCountDistinct.h \
	    src/operator/FileSinkRunGatedCountDistinct.cpp\
	    build/dep/operator/FileSinkRunGatedCountDistinct.dep \
	    src/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.h \
	    src/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.h \
	    src/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.h \
	    src/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.h  \
	    build/cppOptions \
	    | build/operator
	@echo ' [CXX-operator] FileSinkRunGatedCountDistinct'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FileSinkRunGatedCountDistinct.cpp

-include build/operator/FiveStageCountByDistinct/aggOut1/CountByDistinctAggregate.d
build/operator/FiveStageCountByDistinct/aggOut1/CountByDistinctAggregate.o: \
	    src/operator/FiveStageCountByDistinct/aggOut1/CountByDistinctAggregate.h \
	    src/operator/FiveStageCountByDistinct/aggOut1/CountByDistinctAggregate.cpp\
	    build/dep/operator/FiveStageCountByDistinct/aggOut1/CountByDistinctAggregate.dep  \
	    build/cppOptions \
	    | build/operator/FiveStageCountByDistinct/aggOut1
	@echo ' [CXX-operator] FiveStageCountByDistinct.aggOut1.CountByDistinctAggregate'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FiveStageCountByDistinct/aggOut1/CountByDistinctAggregate.cpp

-include build/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated/oStream.d
build/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated/oStream.o: \
	    src/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated/oStream.h \
	    src/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated/oStream.cpp\
	    build/dep/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated/oStream.dep \
	    src/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.h  \
	    build/cppOptions \
	    | build/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated
	@echo ' [CXX-operator] FiveStageCountByDistinct.aggOut1.ClkStrmPunctuated.oStream'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated/oStream.cpp

-include build/operator/FiveStageCountByDistinct/aggOut2/CountByDistinctCascadedAggregate.d
build/operator/FiveStageCountByDistinct/aggOut2/CountByDistinctCascadedAggregate.o: \
	    src/operator/FiveStageCountByDistinct/aggOut2/CountByDistinctCascadedAggregate.h \
	    src/operator/FiveStageCountByDistinct/aggOut2/CountByDistinctCascadedAggregate.cpp\
	    build/dep/operator/FiveStageCountByDistinct/aggOut2/CountByDistinctCascadedAggregate.dep \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.h  \
	    build/cppOptions \
	    | build/operator/FiveStageCountByDistinct/aggOut2
	@echo ' [CXX-operator] FiveStageCountByDistinct.aggOut2.CountByDistinctCascadedAggregate'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FiveStageCountByDistinct/aggOut2/CountByDistinctCascadedAggregate.cpp

-include build/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream/oStream.d
build/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream/oStream.o: \
	    src/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream/oStream.h \
	    src/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream/oStream.cpp\
	    build/dep/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream/oStream.dep \
	    src/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.h  \
	    build/cppOptions \
	    | build/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream
	@echo ' [CXX-operator] FiveStageCountByDistinct.aggOut2.PunctuatedAggregatedInputStream.oStream'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream/oStream.cpp

-include build/operator/RunGated/outputStream.d
build/operator/RunGated/outputStream.o: \
	    src/operator/RunGated/outputStream.h \
	    src/operator/RunGated/outputStream.cpp\
	    build/dep/operator/RunGated/outputStream.dep \
	    src/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.h  \
	    build/cppOptions \
	    | build/operator/RunGated
	@echo ' [CXX-operator] RunGated.outputStream'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/RunGated/outputStream.cpp

-include build/operator/FiveStageCountDistinctAggregateAlias/agg1.d
build/operator/FiveStageCountDistinctAggregateAlias/agg1.o: \
	    src/operator/FiveStageCountDistinctAggregateAlias/agg1.h \
	    src/operator/FiveStageCountDistinctAggregateAlias/agg1.cpp\
	    build/dep/operator/FiveStageCountDistinctAggregateAlias/agg1.dep  \
	    build/cppOptions \
	    | build/operator/FiveStageCountDistinctAggregateAlias
	@echo ' [CXX-operator] FiveStageCountDistinctAggregateAlias.agg1'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FiveStageCountDistinctAggregateAlias/agg1.cpp

-include build/operator/FiveStageCountDistinctAggregateAlias/aggOut1/CountDistinctAggregate.d
build/operator/FiveStageCountDistinctAggregateAlias/aggOut1/CountDistinctAggregate.o: \
	    src/operator/FiveStageCountDistinctAggregateAlias/aggOut1/CountDistinctAggregate.h \
	    src/operator/FiveStageCountDistinctAggregateAlias/aggOut1/CountDistinctAggregate.cpp\
	    build/dep/operator/FiveStageCountDistinctAggregateAlias/aggOut1/CountDistinctAggregate.dep  \
	    build/cppOptions \
	    | build/operator/FiveStageCountDistinctAggregateAlias/aggOut1
	@echo ' [CXX-operator] FiveStageCountDistinctAggregateAlias.aggOut1.CountDistinctAggregate'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FiveStageCountDistinctAggregateAlias/aggOut1/CountDistinctAggregate.cpp

-include build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/CountDistinctCascadedAggregate.d
build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/CountDistinctCascadedAggregate.o: \
	    src/operator/FiveStageCountDistinctAggregateAlias/aggOut2/CountDistinctCascadedAggregate.h \
	    src/operator/FiveStageCountDistinctAggregateAlias/aggOut2/CountDistinctCascadedAggregate.cpp\
	    build/dep/operator/FiveStageCountDistinctAggregateAlias/aggOut2/CountDistinctCascadedAggregate.dep \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.h  \
	    build/cppOptions \
	    | build/operator/FiveStageCountDistinctAggregateAlias/aggOut2
	@echo ' [CXX-operator] FiveStageCountDistinctAggregateAlias.aggOut2.CountDistinctCascadedAggregate'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FiveStageCountDistinctAggregateAlias/aggOut2/CountDistinctCascadedAggregate.cpp

-include build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream/oStream.d
build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream/oStream.o: \
	    src/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream/oStream.h \
	    src/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream/oStream.cpp\
	    build/dep/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream/oStream.dep \
	    src/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.h  \
	    build/cppOptions \
	    | build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream
	@echo ' [CXX-operator] FiveStageCountDistinctAggregateAlias.aggOut2.PunctuatedAg...dInputStream.oStream'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream/oStream.cpp

-include build/operator/RunGatedCountDistinct/outputStream.d
build/operator/RunGatedCountDistinct/outputStream.o: \
	    src/operator/RunGatedCountDistinct/outputStream.h \
	    src/operator/RunGatedCountDistinct/outputStream.cpp\
	    build/dep/operator/RunGatedCountDistinct/outputStream.dep \
	    src/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.h  \
	    build/cppOptions \
	    | build/operator/RunGatedCountDistinct
	@echo ' [CXX-operator] RunGatedCountDistinct.outputStream'
	@$(CXX) -o $@ -MD -I /opt/ibm/InfoSphere_Streams/4.2.1.1/toolkits/spl/impl/nl/include -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" -c $(SPL_CXXFLAGS) src/operator/RunGatedCountDistinct/outputStream.cpp

build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream:
	-@mkdir -m 755 -p build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream

build/operator:
	-@mkdir -m 755 -p build/operator

build/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream:
	-@mkdir -m 755 -p build/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream

build/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated:
	-@mkdir -m 755 -p build/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated

build/operator/FiveStageCountDistinctAggregateAlias/aggOut2:
	-@mkdir -m 755 -p build/operator/FiveStageCountDistinctAggregateAlias/aggOut2

build/operator/FiveStageCountDistinctAggregateAlias/aggOut1:
	-@mkdir -m 755 -p build/operator/FiveStageCountDistinctAggregateAlias/aggOut1

build/operator/FiveStageCountDistinctAggregateAlias:
	-@mkdir -m 755 -p build/operator/FiveStageCountDistinctAggregateAlias

build/operator/RunGatedCountDistinct:
	-@mkdir -m 755 -p build/operator/RunGatedCountDistinct

build/operator/RunGated:
	-@mkdir -m 755 -p build/operator/RunGated

build/operator/FiveStageCountByDistinct/aggOut2:
	-@mkdir -m 755 -p build/operator/FiveStageCountByDistinct/aggOut2

build/operator/FiveStageCountByDistinct/aggOut1:
	-@mkdir -m 755 -p build/operator/FiveStageCountByDistinct/aggOut1

functions: $(SPL_FUNCTIONS)

-include build/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.d
build/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.o: \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.cpp\
	    build/dep/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.dep \
	    build/cppOptions \
	    | build/function/com/ibm/streamsx/clickstream/aggregate
	@echo ' [CXX-function] com.ibm.streamsx.clickstream.aggregate::itemCountResult'
	@$(CXX) -o $@ -c -MD -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" $(SPL_CXXFLAGS) src/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.cpp

-include build/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.d
build/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.o: \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.cpp\
	    build/dep/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.dep \
	    build/cppOptions \
	    | build/function/com/ibm/streamsx/clickstream/aggregate
	@echo ' [CXX-function] com.ibm.streamsx.clickstream.aggregate::itemCountInit'
	@$(CXX) -o $@ -c -MD -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" $(SPL_CXXFLAGS) src/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.cpp

-include build/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.d
build/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.o: \
	    src/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.cpp\
	    build/dep/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.dep \
	    build/cppOptions \
	    | build/function/com/ibm/streamsx/clickstream/aggregate
	@echo ' [CXX-function] com.ibm.streamsx.clickstream.aggregate::TotalItemCountResult'
	@$(CXX) -o $@ -c -MD -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" $(SPL_CXXFLAGS) src/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.cpp

-include build/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.d
build/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.o: \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.cpp\
	    build/dep/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.dep \
	    build/cppOptions \
	    | build/function/com/ibm/streamsx/clickstream/aggregate
	@echo ' [CXX-function] com.ibm.streamsx.clickstream.aggregate::itemListResult'
	@$(CXX) -o $@ -c -MD -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" $(SPL_CXXFLAGS) src/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.cpp

-include build/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.d
build/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.o: \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.cpp\
	    build/dep/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.dep \
	    build/cppOptions \
	    | build/function/com/ibm/streamsx/clickstream/aggregate
	@echo ' [CXX-function] com.ibm.streamsx.clickstream.aggregate::itemListProcess'
	@$(CXX) -o $@ -c -MD -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" $(SPL_CXXFLAGS) src/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.cpp

-include build/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.d
build/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.o: \
	    src/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.cpp\
	    build/dep/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.dep \
	    build/cppOptions \
	    | build/function/com/ibm/streamsx/clickstream/aggregate
	@echo ' [CXX-function] com.ibm.streamsx.clickstream.aggregate::CountDistinctItemResult'
	@$(CXX) -o $@ -c -MD -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" $(SPL_CXXFLAGS) src/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.cpp

-include build/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.d
build/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.o: \
	    src/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.cpp\
	    build/dep/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.dep \
	    build/cppOptions \
	    | build/function/com/ibm/streamsx/clickstream/aggregate
	@echo ' [CXX-function] com.ibm.streamsx.clickstream.aggregate::dummyProcess'
	@$(CXX) -o $@ -c -MD -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" $(SPL_CXXFLAGS) src/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.cpp

-include build/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.d
build/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.o: \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.cpp\
	    build/dep/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.dep \
	    build/cppOptions \
	    | build/function/com/ibm/streamsx/clickstream/aggregate
	@echo ' [CXX-function] com.ibm.streamsx.clickstream.aggregate::itemCountProcess'
	@$(CXX) -o $@ -c -MD -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" $(SPL_CXXFLAGS) src/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.cpp

-include build/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.d
build/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.o: \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.h \
	    src/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.cpp\
	    build/dep/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.dep \
	    build/cppOptions \
	    | build/function/com/ibm/streamsx/clickstream/aggregate
	@echo ' [CXX-function] com.ibm.streamsx.clickstream.aggregate::itemListInit'
	@$(CXX) -o $@ -c -MD -DSPLJAVAFUNCTION_ADL_FILENAME=\"com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.adl\" $(SPL_CXXFLAGS) src/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.cpp

build/function/com/ibm/streamsx/clickstream/aggregate:
	-@mkdir -m 755 -p build/function/com/ibm/streamsx/clickstream/aggregate

sos: $(SPL_SO_BINS)

SOThrottleClkStm = \
	    build/operator/ThrottleClkStm.o \
	    build/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.o 

bin/ThrottleClkStm.so: \
	$(SOThrottleClkStm) \
	build/dep/ThrottleClkStm.so \
	build/ldOptions
	@echo ' [LD-so] so ThrottleClkStm'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/ThrottleClkStm.so -fPIC -shared $(SOThrottleClkStm) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFiveStageCountByDistinctAggregateStream = \
	    build/operator/FiveStageCountByDistinctAggregateStream.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o 

bin/FiveStageCountByDistinctAggregateStream.so: \
	$(SOFiveStageCountByDistinctAggregateStream) \
	build/dep/FiveStageCountByDistinctAggregateStream.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountByDistinctAggregateStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountByDistinctAggregateStream.so -fPIC -shared $(SOFiveStageCountByDistinctAggregateStream) $(SPL_LDFLAGS)

SOFileSinkRunGated = \
	    build/operator/FileSinkRunGated.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o \
	    build/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.o \
	    build/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.o \
	    build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o 

bin/FileSinkRunGated.so: \
	$(SOFileSinkRunGated) \
	build/dep/FileSinkRunGated.so \
	build/ldOptions
	@echo ' [LD-so] so FileSinkRunGated'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FileSinkRunGated.so -fPIC -shared $(SOFileSinkRunGated) -lstreams-stdtk-runtime -lstreams_boost_iostreams -lstreams_boost_filesystem -lstreams_boost_system $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregate = \
	    build/operator/FiveStageCountDistinctAggregate.o \
	    build/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.o 

bin/FiveStageCountDistinctAggregate.so: \
	$(SOFiveStageCountDistinctAggregate) \
	build/dep/FiveStageCountDistinctAggregate.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregate'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregate.so -fPIC -shared $(SOFiveStageCountDistinctAggregate) $(SPL_LDFLAGS)

SOFileSinkRunGatedCountDistinct = \
	    build/operator/FileSinkRunGatedCountDistinct.o \
	    build/type/BeJyrNI43qcrJTDJJr8osME0CEkYARW8GD7.o \
	    build/type/BeJyrNIs3LSjNSy4xTc4vzSsxKc6sSjUpycxNNU_0pzEvMzUw2zUstSy0CACk7A8P.o \
	    build/type/BeJyrNI03Ti4uMy6pKDFOyswzTcrJT842ycnMSwUAf_1wJCo.o \
	    build/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.o 

bin/FileSinkRunGatedCountDistinct.so: \
	$(SOFileSinkRunGatedCountDistinct) \
	build/dep/FileSinkRunGatedCountDistinct.so \
	build/ldOptions
	@echo ' [LD-so] so FileSinkRunGatedCountDistinct'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FileSinkRunGatedCountDistinct.so -fPIC -shared $(SOFileSinkRunGatedCountDistinct) -lstreams-stdtk-runtime -lstreams_boost_iostreams -lstreams_boost_filesystem -lstreams_boost_system $(SPL_LDFLAGS)

SOFiveStageCountByDistinct.aggOut1.CountByDistinctAggregate = \
	    build/operator/FiveStageCountByDistinct/aggOut1/CountByDistinctAggregate.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o \
	    build/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.o 

bin/FiveStageCountByDistinct.aggOut1.CountByDistinctAggregate.so: \
	$(SOFiveStageCountByDistinct.aggOut1.CountByDistinctAggregate) \
	build/dep/FiveStageCountByDistinct.aggOut1.CountByDistinctAggregate.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountByDistinct.aggOut1.CountByDistinctAggregate'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountByDistinct.aggOut1.CountByDistinctAggregate.so -fPIC -shared $(SOFiveStageCountByDistinct.aggOut1.CountByDistinctAggregate) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFiveStageCountByDistinct.aggOut1.ClkStrmPunctuated.oStream = \
	    build/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated/oStream.o \
	    build/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.o \
	    build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o 

bin/FiveStageCountByDistinct.aggOut1.ClkStrmPunctuated.oStream.so: \
	$(SOFiveStageCountByDistinct.aggOut1.ClkStrmPunctuated.oStream) \
	build/dep/FiveStageCountByDistinct.aggOut1.ClkStrmPunctuated.oStream.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountByDistinct.aggOut1.ClkStrmPunctuated.oStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountByDistinct.aggOut1.ClkStrmPunctuated.oStream.so -fPIC -shared $(SOFiveStageCountByDistinct.aggOut1.ClkStrmPunctuated.oStream) $(SPL_LDFLAGS)

SOFiveStageCountByDistinct.aggOut2.CountByDistinctCascadedAggregate = \
	    build/operator/FiveStageCountByDistinct/aggOut2/CountByDistinctCascadedAggregate.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o 

bin/FiveStageCountByDistinct.aggOut2.CountByDistinctCascadedAggregate.so: \
	$(SOFiveStageCountByDistinct.aggOut2.CountByDistinctCascadedAggregate) \
	build/dep/FiveStageCountByDistinct.aggOut2.CountByDistinctCascadedAggregate.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountByDistinct.aggOut2.CountByDistinctCascadedAggregate'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountByDistinct.aggOut2.CountByDistinctCascadedAggregate.so -fPIC -shared $(SOFiveStageCountByDistinct.aggOut2.CountByDistinctCascadedAggregate) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFiveStageCountByDistinct.aggOut2.PunctuatedAggregatedInputStream.oStream = \
	    build/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream/oStream.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o \
	    build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o 

bin/FiveStageCountByDistinct.aggOut2.PunctuatedAggregatedInputStream.oStream.so: \
	$(SOFiveStageCountByDistinct.aggOut2.PunctuatedAggregatedInputStream.oStream) \
	build/dep/FiveStageCountByDistinct.aggOut2.PunctuatedAggregatedInputStream.oStream.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountByDistinct.aggOut2.PunctuatedAggregatedInputStream.oStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountByDistinct.aggOut2.PunctuatedAggregatedInputStream.oStream.so -fPIC -shared $(SOFiveStageCountByDistinct.aggOut2.PunctuatedAggregatedInputStream.oStream) $(SPL_LDFLAGS)

SOFiveStageCountByDistinct.aggOut3.CountByDistinctCascadedAggregate = \
	    build/operator/FiveStageCountByDistinct/aggOut2/CountByDistinctCascadedAggregate.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o 

bin/FiveStageCountByDistinct.aggOut3.CountByDistinctCascadedAggregate.so: \
	$(SOFiveStageCountByDistinct.aggOut3.CountByDistinctCascadedAggregate) \
	build/dep/FiveStageCountByDistinct.aggOut3.CountByDistinctCascadedAggregate.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountByDistinct.aggOut3.CountByDistinctCascadedAggregate'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountByDistinct.aggOut3.CountByDistinctCascadedAggregate.so -fPIC -shared $(SOFiveStageCountByDistinct.aggOut3.CountByDistinctCascadedAggregate) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFiveStageCountByDistinct.aggOut3.PunctuatedAggregatedInputStream.oStream = \
	    build/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream/oStream.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o \
	    build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o 

bin/FiveStageCountByDistinct.aggOut3.PunctuatedAggregatedInputStream.oStream.so: \
	$(SOFiveStageCountByDistinct.aggOut3.PunctuatedAggregatedInputStream.oStream) \
	build/dep/FiveStageCountByDistinct.aggOut3.PunctuatedAggregatedInputStream.oStream.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountByDistinct.aggOut3.PunctuatedAggregatedInputStream.oStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountByDistinct.aggOut3.PunctuatedAggregatedInputStream.oStream.so -fPIC -shared $(SOFiveStageCountByDistinct.aggOut3.PunctuatedAggregatedInputStream.oStream) $(SPL_LDFLAGS)

SOFiveStageCountByDistinct.aggOut4.CountByDistinctCascadedAggregate = \
	    build/operator/FiveStageCountByDistinct/aggOut2/CountByDistinctCascadedAggregate.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o 

bin/FiveStageCountByDistinct.aggOut4.CountByDistinctCascadedAggregate.so: \
	$(SOFiveStageCountByDistinct.aggOut4.CountByDistinctCascadedAggregate) \
	build/dep/FiveStageCountByDistinct.aggOut4.CountByDistinctCascadedAggregate.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountByDistinct.aggOut4.CountByDistinctCascadedAggregate'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountByDistinct.aggOut4.CountByDistinctCascadedAggregate.so -fPIC -shared $(SOFiveStageCountByDistinct.aggOut4.CountByDistinctCascadedAggregate) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFiveStageCountByDistinct.aggOut4.PunctuatedAggregatedInputStream.oStream = \
	    build/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream/oStream.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o \
	    build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o 

bin/FiveStageCountByDistinct.aggOut4.PunctuatedAggregatedInputStream.oStream.so: \
	$(SOFiveStageCountByDistinct.aggOut4.PunctuatedAggregatedInputStream.oStream) \
	build/dep/FiveStageCountByDistinct.aggOut4.PunctuatedAggregatedInputStream.oStream.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountByDistinct.aggOut4.PunctuatedAggregatedInputStream.oStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountByDistinct.aggOut4.PunctuatedAggregatedInputStream.oStream.so -fPIC -shared $(SOFiveStageCountByDistinct.aggOut4.PunctuatedAggregatedInputStream.oStream) $(SPL_LDFLAGS)

SOFiveStageCountByDistinct.aggOut5.CountByDistinctCascadedAggregate = \
	    build/operator/FiveStageCountByDistinct/aggOut2/CountByDistinctCascadedAggregate.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o 

bin/FiveStageCountByDistinct.aggOut5.CountByDistinctCascadedAggregate.so: \
	$(SOFiveStageCountByDistinct.aggOut5.CountByDistinctCascadedAggregate) \
	build/dep/FiveStageCountByDistinct.aggOut5.CountByDistinctCascadedAggregate.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountByDistinct.aggOut5.CountByDistinctCascadedAggregate'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountByDistinct.aggOut5.CountByDistinctCascadedAggregate.so -fPIC -shared $(SOFiveStageCountByDistinct.aggOut5.CountByDistinctCascadedAggregate) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFiveStageCountByDistinct.aggOut5.PunctuatedAggregatedInputStream.oStream = \
	    build/operator/FiveStageCountByDistinct/aggOut2/PunctuatedAggregatedInputStream/oStream.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o \
	    build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o 

bin/FiveStageCountByDistinct.aggOut5.PunctuatedAggregatedInputStream.oStream.so: \
	$(SOFiveStageCountByDistinct.aggOut5.PunctuatedAggregatedInputStream.oStream) \
	build/dep/FiveStageCountByDistinct.aggOut5.PunctuatedAggregatedInputStream.oStream.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountByDistinct.aggOut5.PunctuatedAggregatedInputStream.oStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountByDistinct.aggOut5.PunctuatedAggregatedInputStream.oStream.so -fPIC -shared $(SOFiveStageCountByDistinct.aggOut5.PunctuatedAggregatedInputStream.oStream) $(SPL_LDFLAGS)

SORunGated.outputStream = \
	    build/operator/RunGated/outputStream.o \
	    build/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.o \
	    build/type/BeJwrsSg2zUlMSs0ptkwvyi8t8EvMBbINLTNLUnOd83NyUpNLXDKLSzLzkktyMmHCpXklTpUwYU9Dy7TMouKSkMzc1OKSxNwCz7zg1GRPQ5MSNAGz8mS4GjeQDk9DUyQhn8TiEgAyhTZv.o 

bin/RunGated.outputStream.so: \
	$(SORunGated.outputStream) \
	build/dep/RunGated.outputStream.so \
	build/ldOptions
	@echo ' [LD-so] so RunGated.outputStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/RunGated.outputStream.so -fPIC -shared $(SORunGated.outputStream) $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.agg1 = \
	    build/operator/FiveStageCountDistinctAggregateAlias/agg1.o \
	    build/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.agg1.so: \
	$(SOFiveStageCountDistinctAggregateAlias.agg1) \
	build/dep/FiveStageCountDistinctAggregateAlias.agg1.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.agg1'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.agg1.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.agg1) $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.agg2 = \
	    build/operator/FiveStageCountDistinctAggregateAlias/agg1.o \
	    build/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.agg2.so: \
	$(SOFiveStageCountDistinctAggregateAlias.agg2) \
	build/dep/FiveStageCountDistinctAggregateAlias.agg2.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.agg2'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.agg2.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.agg2) $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.agg3 = \
	    build/operator/FiveStageCountDistinctAggregateAlias/agg1.o \
	    build/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.agg3.so: \
	$(SOFiveStageCountDistinctAggregateAlias.agg3) \
	build/dep/FiveStageCountDistinctAggregateAlias.agg3.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.agg3'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.agg3.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.agg3) $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.agg4 = \
	    build/operator/FiveStageCountDistinctAggregateAlias/agg1.o \
	    build/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.agg4.so: \
	$(SOFiveStageCountDistinctAggregateAlias.agg4) \
	build/dep/FiveStageCountDistinctAggregateAlias.agg4.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.agg4'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.agg4.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.agg4) $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.agg5 = \
	    build/operator/FiveStageCountDistinctAggregateAlias/agg1.o \
	    build/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.agg5.so: \
	$(SOFiveStageCountDistinctAggregateAlias.agg5) \
	build/dep/FiveStageCountDistinctAggregateAlias.agg5.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.agg5'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.agg5.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.agg5) $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.aggOut1.CountDistinctAggregate = \
	    build/operator/FiveStageCountDistinctAggregateAlias/aggOut1/CountDistinctAggregate.o \
	    build/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.aggOut1.CountDistinctAggregate.so: \
	$(SOFiveStageCountDistinctAggregateAlias.aggOut1.CountDistinctAggregate) \
	build/dep/FiveStageCountDistinctAggregateAlias.aggOut1.CountDistinctAggregate.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.aggOut1.CountDistinctAggregate'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.aggOut1.CountDistinctAggregate.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.aggOut1.CountDistinctAggregate) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.aggOut1.ClkStrmPunctuated.oStream = \
	    build/operator/FiveStageCountByDistinct/aggOut1/ClkStrmPunctuated/oStream.o \
	    build/type/BeJxdj0sOgzAMRK_0EoeoRkNh3bwXjVhbko9hpxe1JUdMFy5l5sp4NYAKgohY9Z5RFoTPxjGrOJ4U7bUIr8puDoe2Jxx4smtswZSHG_0MTZ6co2Db8_0FD_1XS3UQY68ooRG37kosoiaB7Ioq9CnHpdQlOM9Vo0Vyxq_0Y9xGGVp0i3yf0UcVP75o_09E8HdAFYCq.o \
	    build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o 

bin/FiveStageCountDistinctAggregateAlias.aggOut1.ClkStrmPunctuated.oStream.so: \
	$(SOFiveStageCountDistinctAggregateAlias.aggOut1.ClkStrmPunctuated.oStream) \
	build/dep/FiveStageCountDistinctAggregateAlias.aggOut1.ClkStrmPunctuated.oStream.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.aggOut1.ClkStrmPunctuated.oStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.aggOut1.ClkStrmPunctuated.oStream.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.aggOut1.ClkStrmPunctuated.oStream) $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.aggOut2.CountDistinctCascadedAggregate = \
	    build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/CountDistinctCascadedAggregate.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.aggOut2.CountDistinctCascadedAggregate.so: \
	$(SOFiveStageCountDistinctAggregateAlias.aggOut2.CountDistinctCascadedAggregate) \
	build/dep/FiveStageCountDistinctAggregateAlias.aggOut2.CountDistinctCascadedAggregate.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.aggOut2.CountDistinctCascadedAggregate'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.aggOut2.CountDistinctCascadedAggregate.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.aggOut2.CountDistinctCascadedAggregate) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.aggOut2.PunctuatedAggregatedInputStream.oStream = \
	    build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream/oStream.o \
	    build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.aggOut2.PunctuatedAggregatedInputStream.oStream.so: \
	$(SOFiveStageCountDistinctAggregateAlias.aggOut2.PunctuatedAggregatedInputStream.oStream) \
	build/dep/FiveStageCountDistinctAggregateAlias.aggOut2.PunctuatedAggregatedInputStream.oStream.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.aggOut2.PunctuatedAggregatedInputStream.oStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.aggOut2.PunctuatedAggregatedInputStream.oStream.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.aggOut2.PunctuatedAggregatedInputStream.oStream) $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.aggOut3.CountDistinctCascadedAggregate = \
	    build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/CountDistinctCascadedAggregate.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.aggOut3.CountDistinctCascadedAggregate.so: \
	$(SOFiveStageCountDistinctAggregateAlias.aggOut3.CountDistinctCascadedAggregate) \
	build/dep/FiveStageCountDistinctAggregateAlias.aggOut3.CountDistinctCascadedAggregate.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.aggOut3.CountDistinctCascadedAggregate'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.aggOut3.CountDistinctCascadedAggregate.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.aggOut3.CountDistinctCascadedAggregate) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.aggOut3.PunctuatedAggregatedInputStream.oStream = \
	    build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream/oStream.o \
	    build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.aggOut3.PunctuatedAggregatedInputStream.oStream.so: \
	$(SOFiveStageCountDistinctAggregateAlias.aggOut3.PunctuatedAggregatedInputStream.oStream) \
	build/dep/FiveStageCountDistinctAggregateAlias.aggOut3.PunctuatedAggregatedInputStream.oStream.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.aggOut3.PunctuatedAggregatedInputStream.oStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.aggOut3.PunctuatedAggregatedInputStream.oStream.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.aggOut3.PunctuatedAggregatedInputStream.oStream) $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.aggOut4.CountDistinctCascadedAggregate = \
	    build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/CountDistinctCascadedAggregate.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.aggOut4.CountDistinctCascadedAggregate.so: \
	$(SOFiveStageCountDistinctAggregateAlias.aggOut4.CountDistinctCascadedAggregate) \
	build/dep/FiveStageCountDistinctAggregateAlias.aggOut4.CountDistinctCascadedAggregate.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.aggOut4.CountDistinctCascadedAggregate'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.aggOut4.CountDistinctCascadedAggregate.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.aggOut4.CountDistinctCascadedAggregate) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.aggOut4.PunctuatedAggregatedInputStream.oStream = \
	    build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream/oStream.o \
	    build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.aggOut4.PunctuatedAggregatedInputStream.oStream.so: \
	$(SOFiveStageCountDistinctAggregateAlias.aggOut4.PunctuatedAggregatedInputStream.oStream) \
	build/dep/FiveStageCountDistinctAggregateAlias.aggOut4.PunctuatedAggregatedInputStream.oStream.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.aggOut4.PunctuatedAggregatedInputStream.oStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.aggOut4.PunctuatedAggregatedInputStream.oStream.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.aggOut4.PunctuatedAggregatedInputStream.oStream) $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.aggOut5.CountDistinctCascadedAggregate = \
	    build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/CountDistinctCascadedAggregate.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/CountDistinctItemResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/TotalItemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/dummyProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemCountResult.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListInit.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListProcess.o \
	    build/function/com/ibm/streamsx/clickstream/aggregate/itemListResult.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.aggOut5.CountDistinctCascadedAggregate.so: \
	$(SOFiveStageCountDistinctAggregateAlias.aggOut5.CountDistinctCascadedAggregate) \
	build/dep/FiveStageCountDistinctAggregateAlias.aggOut5.CountDistinctCascadedAggregate.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.aggOut5.CountDistinctCascadedAggregate'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.aggOut5.CountDistinctCascadedAggregate.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.aggOut5.CountDistinctCascadedAggregate) -lstreams-stdtk-runtime $(SPL_LDFLAGS)

SOFiveStageCountDistinctAggregateAlias.aggOut5.PunctuatedAggregatedInputStream.oStream = \
	    build/operator/FiveStageCountDistinctAggregateAlias/aggOut2/PunctuatedAggregatedInputStream/oStream.o \
	    build/type/BeJyrNIo3NArPzEvJL_1dNLMpOLTI0dMvMS8yBcACkegr2.o \
	    build/type/BeJxdy8EKgzAQhOFX6kKt5NqWQkB6qS8Qw1oWNlHcEfHtqwfT0tvw8Q_1oZJWGjtXcexrm8RnStskJON0GVY64i0FyhMrBc8Z1PVioLlrsG3pyvUyGVhIbQhp9fnH0dMYfXJZYmsf_08FT9UBMMH8GZEK9.o 

bin/FiveStageCountDistinctAggregateAlias.aggOut5.PunctuatedAggregatedInputStream.oStream.so: \
	$(SOFiveStageCountDistinctAggregateAlias.aggOut5.PunctuatedAggregatedInputStream.oStream) \
	build/dep/FiveStageCountDistinctAggregateAlias.aggOut5.PunctuatedAggregatedInputStream.oStream.so \
	build/ldOptions
	@echo ' [LD-so] so FiveStageCountDistinctAggregateAlias.aggOut5.PunctuatedAggregatedInputStream.oStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/FiveStageCountDistinctAggregateAlias.aggOut5.PunctuatedAggregatedInputStream.oStream.so -fPIC -shared $(SOFiveStageCountDistinctAggregateAlias.aggOut5.PunctuatedAggregatedInputStream.oStream) $(SPL_LDFLAGS)

SORunGatedCountDistinct.outputStream = \
	    build/operator/RunGatedCountDistinct/outputStream.o \
	    build/type/BeJyrNI03TS0qyi8yKU8syjPJzEvLN01JTSpNNy0pSkxOBQC5eQu5.o \
	    build/type/BeJxdy0EKgCAQRuEzCVm5LgIh2tQFTKYYSJPml64fbSTafryHVvThVjrE7NeZ0_0QCsWoYFLozR_1Qs4OjBppBVZuNLsHAggQvJxpm8VRV_0UN_0_0NMN7WKU_1NDrBAyM6DCg.o 

bin/RunGatedCountDistinct.outputStream.so: \
	$(SORunGatedCountDistinct.outputStream) \
	build/dep/RunGatedCountDistinct.outputStream.so \
	build/ldOptions
	@echo ' [LD-so] so RunGatedCountDistinct.outputStream'
	@$(CXX) $(SPL_CXXFLAGS) -o bin/RunGatedCountDistinct.outputStream.so -fPIC -shared $(SORunGatedCountDistinct.outputStream) $(SPL_LDFLAGS)

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
	@ln -sf standalone bin/com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates
build/standalone:
	-@mkdir -m 755 build/standalone

sablink:

	@ln -sf ../com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.sab bin/sab

bundle: com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.sab

-include build/dep/com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.sab.d
com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.sab: $(SPL_SO_BINS) $(SPL_ADL_FILE) build/dep/com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.sab.d bin/standalone.exe
	@echo ' [Bundle] com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.sab'
	@$(SPL_BUNDLE_BUILDER) $(SPL_OUTPUT_DIR_ROOT) $(SPL_OUTPUT_DIR) $(SPL_ADL_FILE) com.ibm.streamsx.clickstream.Aggregates.ClickstreamAggregates.sab

