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

Some stuff about SPARQL

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
4. [SPARQL Python Library](https://github.com/RDFLib/sparqlwrapper)


## Authors

* **Sander Henning**
* **Frank Meszaros**
* **Joel Pepper**
* **Zach Ponath**
* **Shashank Rajkumar**
* **Skyler Reimer**
* **Ethan Smith**

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
