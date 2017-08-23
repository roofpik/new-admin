import json
import requests
from pprint import pprint


def Num_Info():
	rkey='-KfM5tQ-UKt6DtrWtzeE'
	rtype='micromarket'
	query = {}
	query['query'] = {}
	query['query']['match'] = {}
	query['from'] = 0
	query['size'] = 400
	if rtype=='city':
		query['query']['match']['location.citykey'] = rkey
	if rtype=='micromarket':
		query['query']['match']['location.microkey'] = rkey
	if rtype=='locality':
		query['query']['match']['location.lockey'] = rkey

	esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com'
	r = requests.get(esserver + '/projectnewin_v1/data/_search?', data=json.dumps(query))
	result = json.loads(r.content)['hits']['hits']





	#count proptype

	'''count_ptype=[0,0,0,0]
	for temp in result:
		extemp=temp['_source']['propType']
		for j in extemp:
			if(j=='villa'):
				count_ptype[0]+=1
			if(j=='apartment'):
				count_ptype[1]+=1
			if(j=='penthouse'):
				count_ptype[2]+=1
			if(j=='rowhouse'):
				count_ptype[3]+=1


	for i in range(0,len(count_ptype)):
		print count_ptype[i]'''






	# Count type
	count_type=[0,0,0,0,0,0,0,0]
	avg_type=[0,0,0,0,0,0,0,0]
	



	for temp in result:
		extemp=temp['_source']['score']
		k=-1
		cost=temp['_source']['rentsummary']
		imposed_avg=float((int(cost['max'])+int(cost['min']))/2)
		for j in extemp:
			k=k+1
			if extemp[j]!=0:
				count_type[k]+=1
				avg_type[k]+=imposed_avg

	for i in range(0,len(count_type)):
		print count_type[i]
		avg_type[i]/=count_type[i]
		print avg_type[i]




		




Num_Info()