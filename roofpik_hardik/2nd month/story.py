import json
import requests
from sets import Set
from pprint import pprint

esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com/'
with open('data.json','r') as file:
	d=json.load(file)
var=(d['story']['data']['country']['-K_43TEI8cBodNbwlKqJ']['city'])
ind=0
for i in var:
	#pprint(var[i]['residential'])
	for j in var[i]['residential']:
		for k in var[i]['residential'][j]['items']:
			ind+=1
			payload = json.dumps(var[i]['residential'][j]['items'][k])
			url = esserver + "story/data/"+str(ind)
			r = requests.put(url, data=payload)
