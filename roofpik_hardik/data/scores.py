import json
import requests
from pprint import pprint
def func(val1,val2,count_arr):
	if val1>=7 :
		for j in val2:
			if j=='apartment' :
				count_arr[0]+=1
			if j=='penthouse' :
				count_arr[1]+=1
			if j=='villa' :
				count_arr[2]+=1
		return count_arr


def scores():
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

	#pprint(result[1]['_source']['score'])
	sumarr=[0,0,0,0,0,0,0,0]
	count_apart=0
	count_pent=0
	count_villa=0
	count_arr1=[0,0,0]
	count_arr2=[0,0,0]
	count_arr3=[0,0,0]
	count_arr4=[0,0,0]
	count_arr5=[0,0,0]
	count_arr6=[0,0,0]
	count_arr7=[0,0,0]
	count_arr8=[0,0,0]

	for i in range(0,len(result)):
		temp=result[i]['_source']['score']
		vall=result[i]['_source']['propType']
		if temp['affordable']>=7 :
			for j in vall:
				if j=='apartment' :
					if vall[j]== True :
						count_arr1[0]+=1
				if j=='penthouse' :
					if vall[j]== True :
						count_arr1[1]+=1
				if j=='villa' :
					if vall[j]== True :
						count_arr1[2]+=1
		if temp['bachelors']>=7 :
			for j in vall:
				if j=='apartment' :
					count_arr2[0]+=1
				if j=='penthouse' :
					count_arr2[1]+=1
				if j=='villa' :
					count_arr2[2]+=1
		if temp['bestAmenities']>=7 :
			for j in vall:
				if j=='apartment' :
					count_arr3[0]+=1
				if j=='penthouse' :
					count_arr3[1]+=1
				if j=='villa' :
					count_arr3[2]+=1
		if temp['downtown']>=7 :
			for j in vall:
				if j=='apartment' :
					count_arr4[0]+=1
				if j=='penthouse' :
					count_arr4[1]+=1
				if j=='villa' :
					count_arr4[2]+=1
		if temp['luxury']>=7 :
			for j in vall:
				if j=='apartment' :
					count_arr5[0]+=1
				if j=='penthouse' :
					count_arr5[1]+=1
				if j=='villa' :
					count_arr5[2]+=1
		if temp['petFriendly']>=7 :
			for j in vall:
				if j=='apartment' :
					count_arr6[0]+=1
				if j=='penthouse' :
					count_arr6[1]+=1
				if j=='villa' :
					count_arr6[2]+=1
		if temp['seniorLiving']>=7 :
			for j in vall:
				if j=='apartment' :
					count_arr7[0]+=1
				if j=='penthouse' :
					count_arr7[1]+=1
				if j=='villa' :
					count_arr7[2]+=1
		if temp['ultraLuxury']>=7 :
			for j in vall:
				if j=='apartment' :
					count_arr8[0]+=1
				if j=='penthouse' :
					count_arr8[1]+=1
				if j=='villa' :
					count_arr8[2]+=1
		
		'''count_arr1=func(,vall,count_arr1)
		count_arr2=func(temp['bachelors'],vall,count_arr2)
		count_arr3=func(temp['bestAmenities'],vall,count_arr3)
		count_arr4=func(temp['downtown'],vall,count_arr4)
		count_arr5=func(temp['luxury'],vall,count_arr5)
		count_arr6=func(temp['petFriendly'],vall,count_arr6)
		count_arr7=func(temp['seniorLiving'],vall,count_arr7)
		count_arr8=func(temp['ultraLuxury'],vall,count_arr8)
		


		if result[i]['_source']['score']['affordable']>=7:
			for j in vall:
				if j=='apartment' :
					count_arr+=1
				if j=='penthouse' :
					count_pent+=1
				if j=='villa' :
					count_villa+=1'''
	print count_arr1[0], count_arr1[1],count_arr1[2]
	print count_arr2[0], count_arr2[1],count_arr2[2]
	print count_arr3[0], count_arr3[1],count_arr3[2]
	print count_arr4[0], count_arr4[1],count_arr4[2]
	print count_arr5[0], count_arr5[1],count_arr5[2]

	print count_arr6[0], count_arr6[1],count_arr6[2]

	print count_arr7[0], count_arr7[1],count_arr7[2]
	print count_arr8[0], count_arr8[1],count_arr8[2]



		




















scores()