import json
import requests
from sets import Set
from pprint import pprint


with open('data.json','r') as file:
	d=json.load(file)

temp =d['project']['country']['-K_43TEI8cBodNbwlKqJ']['city']

'''for i in temp:
	#print temp[i]
	city_key=i
	for j in temp[i]['residential']['micromarket']:
		var=temp[i]['residential']['micromarket']
		micro_key=j
		for k in var[j]['locality']:
			#print k
			locality_key=k
			for l in var[j]['locality'][k]['projects']:
				project_key=l
				tem=var[j]['locality'][k]['projects'][l]
				print(tem['scores'])'''


#print(len(temp))
for i in temp:
	for j in temp[i]['residential']['micromarket']:
		for k in temp[i]['residential']['micromarket'][j]['locality']:
			for l in temp[i]['residential']['micromarket'][j]['locality'][k]['projects']:
				#pprint(temp[i]['residential']['micromarket'][j]['locality'][k]['projects'][l][a.encode('ascii','ignore')])
				for m in temp[i]['residential']['micromarket'][j]['locality'][k]['projects'][l]:
					pprint(temp[i]['residential']['micromarket'][j]['locality'][k]['projects'][l]['propertyTypes'])
					
				
					
					

