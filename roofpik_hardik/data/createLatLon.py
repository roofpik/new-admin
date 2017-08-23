import json
import requests
from sets import Set
from pprint import pprint

def createLatLon():
	tlat= 28.403868
	tlon= 77.044919
	
	esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com/distance_search/location/_search?'
	data='{"query": {"bool": {"must": { "match_all": {}},"filter": {"geo_distance": {"distance": "10km","pin.location": {"lat":'+ str(tlat)+',"lon":'+ str(tlon)+'}}}}}}' 

	response = requests.get(esserver, data=data)

	d=response.json()
	result = (d['hits']['hits'])
	#print len(result)
	pprint(result)



createLatLon()