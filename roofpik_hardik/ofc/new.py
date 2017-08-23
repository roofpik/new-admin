import json
import requests
from pprint import pprint

with open('data.json') as json_data:
	d=json.load(json_data)

temp=d['projects']['-KYJONgh0P98xoyPPYm9']['cghs']
pprint(temp)
d=set()
for i in temp:
	id=i
	for j in temp[i]:
		if j == 'amenities':
			for i1 in temp[i][j]:
				print i1
			print('-------------------------------------------')

print(d)