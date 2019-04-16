from SPARQLWrapper import SPARQLWrapper, JSON
import pprint

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
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
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

pprint.pprint(results)
