import json
import requests

def convert_To_FirstPoint(a):
	 return round(a,1)

def calc1(coun,nume):
	if coun!=0 :
		return str(convert_To_FirstPoint(float(nume)/float(coun)))
	else :	
		return 'False'


def reviewSummary():
	_key = '-KYJONgh0P98xoyPPYm9'
	query = {}
	query['query'] = {}
	query['query']['match'] = {}
	query['query']['match']['project.city'] = _key
	query['from'] = 0
	query['size'] = 20
	# query = {
	# 		   "query": {
	# 		      "match": {
	# 		         "project.key": _key
	# 		      }
	# 		   }
	# 		}
	items = []
	esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com'
	r = requests.get(esserver + '/allreviewsin/data/_search?', data=json.dumps(query))
	result = json.loads(r.content)['hits']['hits']
	print(len(result))
	#print result
	#print json.dumps(result, indent=4, separators=(',', ': '))
	#print result[0]['_source']['mainrating']
	#print result[1]['_source']['mainrating']
	'''count_security=0
	count_infra=0
	count_amenties=0
	count_greenry=0
	count_parking=0
	sum_in=0
	sum_sec=0
	sum_am=0
	sum_gr=0
	sum_prk=0
	for i in range(0,len(result)):
		temp=result[i]['_source']['mainrating']
		if (temp['infrastructure']!=False) :
		 count_infra += 1
		 sum_in+=int(temp['infrastructure'])
		if (temp['security']!=False) :
		 count_security += 1
		 sum_sec+=int(temp['security'])
		if (temp['amenities']!=False) :
		 count_amenties += 1
		 sum_am+=int(temp['amenities'])
		if (temp['greenry']!=False) :
		 count_greenry += 1
		 sum_gr+=int(temp['greenry'])
		if (temp['parking']!=False) :
		 count_parking += 1
		 sum_prk+=int(temp['parking'])

	
	secur=calc1(count_security,sum_sec)
	infra=calc1(count_infra,sum_in)
	amen=calc1(count_amenties,sum_am)
	green=calc1(count_greenry,sum_gr)
	prk=calc1(count_parking,sum_prk)
	print secur

	

	count_oth=0
	count_ten=0
	count_ow=0
	countarr=[0,0,0,0,0,0]
	for i in range(0,len(result)):
		temp=result[i]['_source']['user']
		if temp['type']=='Tenant' :
			count_ten+=1
		if temp['type']=='Owner' :
			count_ow+=1
		if temp['type']=='Other' :
			count_oth+=1
		temp1=result[i]['_source']['main']['rating']
		countarr[temp1-1]+=1
	calc=0 
	num=0
	for i in range(0,5):
		print countarr[i]
		num+=countarr[i]
		calc+=(i+1)*countarr[i]
	convert_To_FirstPoint(float(calc)/float(num)) 
	print count_ten,count_ow,count_oth'''
	for i in range(0,len(result)):
		pname=result[i]['_source']['project']['name']
		uname=result[i]['_source']['user']['uname']
		mrating=result[i]['_source']['main']['rating']
		title=result[i]['_source']['main']['title']
		detail=result[i]['_source']['main']['detail']
		print pname,uname,mrating,title,detail
		print '----------------------------------------'


	


	



reviewSummary()