# Note:
This page is a work in progress. Comments, criticisms, additions, and alternatives are all welcome. Please contribute to the discussion. Please [contribute to the discussion](https://github.com/IBMStreams/streamsx.clickstream/issues).

# streamsx.clickstream
The IBMStreams/streamsx.clickstream repository is an open source Streams project focused on the development of a toolkit of basic functions and operators to build an application for click or tap stream analytics. It also provides a streaming architecture based sample application for clickstream analytics.

# Overview
The real-time streaming analytics of click or tap streams bears an indispensable significance for digital transformation of all growing enterprises. It provides a way to monitor, qualitatively and quantitatively, the effectiveness of web or mobile applications. In the large scale mobile enterprises environemnt, a real-time clickstreams analytics is imperative to:

- Continously improve customer experience
- Monitor the effectiveness of the web or mobile applications
- Remove frictions from customer journeys
- Positively impact business growth
- Clinch the points of inflection impacting the revenue streams

# General Architecture
A typical IBM Streams based clickstream applicaion is built around several microservice applicaitons as following:

1. Acqusition and Enrichment
    * Clickstreams log/data acqusition
    * Decryption and sterilization
    * Sessions or user level enrichment
2. Hierarchical identification of the events
    * Hierarchical categorization of service flows
    * Events identification and classification
    * Deduplication of events with various hirarcies
    * Transition detection at various hirarcical levels
3. Aggregations and sequencing of events
    * Primary and secondary aggregation
    * Sequancing of event transitions into hirarcical graph
    * Statistical data analytics
4. Common subsequence analytics
    * Dectection and extraction of common subsequences
    * Detection of frictions from customer journeys 

# Toolkit Components
### Clickstream Classification Operator
A scalable and dynamically updated set of classification rules are defined in a JSON file. Each JSON rule specifies string attribute of the input stream, to be matched against a specified string, partial string, or regex. When a rule is matched the specified attributes of the output stream are updated as per the given classification by that rule. 
### Custom aggregate functions for progressive and cascaded aggregates
Instead of “sliding windows aggregates”, cascaded “tumbing window aggregates” are used to produce Count-By-Distinct function.
### Graph generator operator
A custom SPL operator to produce a graph JSON for:
- Customer journey visualization
- Path analytics, e.g. Visit count, abandon count, etc.
