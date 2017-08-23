import requests
import json
from pprint import pprint

def name_search():
	inp='Sispal Vihar'
	query = {}
	query['query'] = {}
	query['query']['match_phrase'] = {}
	query['query']['match_phrase']['project.name'] = inp
	query['from'] = 0
	query['size'] = 2000

	esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com'
	r = requests.get(esserver + '/allreviewsin/data/_search?', data=json.dumps(query))
	result = json.loads(r.content)['hits']['hits']
	res=[]

	for i in range(0,len(result)):
		project=result[i]['_source']['project']
		user=result[i]['_source']['user']
		main=result[i]['_source']['main']
		res.append({'project':project,'user':user,'main':main})

	pprint(res)

name_search()