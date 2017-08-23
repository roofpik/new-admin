import json
import requests
from sets import Set
from pprint import pprint

def populate():
	query = {}
	query['from'] = 0
	query['size'] = 400
	esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com'
	r = requests.get(esserver + '/projectnewin_v1/data/_search?',data=json.dumps(query))
	result = json.loads(r.content)['hits']['hits']
	#pprint(result)
	ind=0
	for i in result:
		ind += 1
		k=i['_source']
		ckey=k['location']['citykey']
		lname=k['location']['locname']
		mkey=k['location']['microkey']
		mname=k['location']['microname']
		lat=k['location']['lat']
		lon=k['location']['lng']
		disp=k['location']['display']
		lkey=k['location']['lockey']
		#print (ckey,lname,mkey,mname,lat,lon,disp)
		esserver1 = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com/distance_search/location/'
		data={"pin":{"citykey":ckey,"locname":lname,"microkey":mkey,"microname":mname,"lockey":lkey,"display":disp,"location":{"lat":lat,"lon":lon}}}
		data1=json.dumps(data)
		r=requests.put(esserver1+str(ind),data=data1)
		






populate()