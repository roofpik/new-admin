import requests
import json

def distinct_name():
	_key = '-KYJONgh0P98xoyPPYm9'
	query = {}
	query['query'] = {}
	query['query']['match'] = {}
	query['query']['match']['project.city'] = _key
	query['from'] = 0
	query['size'] = 2000
	esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com'
	r = requests.get(esserver + '/allreviewsin/data/_search?', data=json.dumps(query))
	result = json.loads(r.content)['hits']['hits']
	print(result[0]['_source']['project']['name'])
	d=set()
	for i in range(0,len(result)):
		d.add(result[i]['_source']['project']['name'])

	print len(d)

	'''with open('distinct.txt','a') as f:
		for i in d:
			f.write(i)
			f.write('\n')'''







distinct_name()