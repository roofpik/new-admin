import json
import requests
from pprint import pprint


with open('req_data1.json','r') as json_data:
	d=json.load(json_data)

#pprint(d['project'])

'''with open('req_data1.json', 'w') as outfile:  
    json.dump(d['project'], outfile,indent=4)'''
sum=0
res={}
temp=d['country']['-K_43TEI8cBodNbwlKqJ']['city']['-KYJONgh0P98xoyPPYm9']['residential']['micromarket']
for i in temp:
	if i!='undefined':
		for j in temp[i]['locality']:
			for k in temp[i]['locality'][j]['projects']:
				print k
				#pprint(temp[i]['locality'][j]['projects'][k])
				res[k] = temp[i]['locality'][j]['projects'][k]
				# res.append({k : )


with open('res_data.json', 'w') as outfile:  
    json.dump(res, outfile,indent=4)				

