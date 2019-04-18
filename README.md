# Using DBPedia with SPARQL

**TODO: Add small introduction paragraph/abstract.**
**TODO: Table of contents**

## DBPedia

DBPedia is a crowd-sourced effort that aims to extract structured data from a variety of different Wikimedia projects. The data is structured as an open knowledge graph (OKG), so it's available to everyone on the web. This critical structured data is published strictly within some "Linked Open Data" guidelines. This Linked Open Data Cloud has grown to become a huge collection of structed data as RDF Predicate/Property Graphs. 

![](https://cdn-images-1.medium.com/max/1600/1*gLsHP-XUPHJJF_uaXzBqDw.png "DBPedia Linked Open Data Cloud")
**Linked Open Data Cloud, circa 2016.** Source: http://lod-cloud.net/versions/2014-08-30/lod-cloud.svg

This data from the Wikimedia projects is exposed in a form that many tools, including natural=-language processing, machine learning, and artificial intellignece, are actually compatible with. Basically, DBPedia enabled the Linked Open Data Cloud to become the huge reference database. Since DBPedia is served as linked data, it can be interacted with in a variety of different ways:

* standard web browsers
* automated crawlers
* **complex queries with SQL-like query languages (e.g. SPARQL)**




## SPARQL

SPARQL is a query language that works on data stored in the Resource Description Framework (RDF) format. RDF data can be thought of as a loose interpretation of key-value data, consisting of subject-predicate-object triplets. These triplets are very similar to MongoDBs "document-key-value" triplets. To simplify in terms of relational databases, the subject is like an entity, the predicate it's columns, and the objects are the actual values for those columns. Unlike relational databases, RDF can have multiple entries per predicate, and even the object data type is heterogenous, though usually implied by the predicate.

What really sets SPARQL apart though, is the ability to use web identifiers for the entities that are being described. This allows for the RDF data to be merged from multiple databases without any sort of intermediate step of mapping terms between them that a relational would require. This means that as long as your data follows the RDF format, you can set upa SPARQL endpoint that basically allows you to be a service provider for your data, and to use data from other endpoints to create a mashup that can be of great use.

## RDF
### Overview
To understand SPARQL, it is important to also understand how an RDF document is
structured. RDF is based around the idea of storing statements, which include 3
required parts: a subject, a predicate, and an object. For example, in the
statement

> The instructor of CSE 5914 is Stephen Boxwell.

* The subject of the statement is CSE 5914
* The predicate is instructor
* The object is Stephen Boxwell

With this in mind, we can consider how this information might be structured
within the general framework of XML.
### Syntax


## Putting it together in Python

First things first. You'll need to install or make your own SPARQL Wrapper. We chose to use a python wrapper

With pip

    $ pip install sparqlwrapper

All of this code can be found in "example.py" in this repository. First you'll need to import the wrapper and make the object. We're using DBPedia's endpoint 

```
from SPARQLWrapper import SPARQLWrapper, JSON
import pprint

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
```

Next we have to set a query 
```
sparql.setQuery(
    """
    SELECT ?name ?birth ?person
    WHERE {
      ?person a dbo:MusicalArtist .
      ?person dbo:birthDate ?birth .
      ?person foaf:name ?name .
    } 
    LIMIT 10
    """
)
```

Then we run the query and format it as JSON for easy mode parsing!
```
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
```

## Sources
1. [DBPedia](https://wiki.dbpedia.org/)
2. [Why is DBPedia Important](https://medium.com/openlink-software-blog/what-is-dbpedia-and-why-is-it-important-d306b5324f90)
3. [SPARQL](https://en.wikipedia.org/wiki/SPARQL)
4. [Cambridge Semantics](https://www.cambridgesemantics.com/blog/semantic-university/learn-sparql/sparql-vs-sql/)
6. [SPARQL Python Library](https://github.com/RDFLib/sparqlwrapper)


## Authors

* **Sander Henning**
* **Frank Meszaros**
* **Joel Pepper**
* **Zach Ponath**
* **Shashank Rajkumar**
* **Skyler Reimer**
* **Ethan Smith**

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
