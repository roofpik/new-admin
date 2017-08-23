import json
import requests
from sets import Set
from pprint import pprint
'''
populating data
esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com/'
with open('data.json','r') as file:
	d=json.load(file)

#pprint(d['blog']['content'])
ind=0
for i in d['blog']['content']['-KgyentIj_hMfxWYt1nJ']['section']:
	ind+=1
	payload = json.dumps(d['blog']['content']['-KgyentIj_hMfxWYt1nJ']['section'][i])
	url = esserver + "my_index2/data/"+str(ind)
	r = requests.put(url, data=payload)
	'''


#testing

esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com/my_index2/data/_search'

data='{"sort": { "updated": "desc"} }'

response = requests.get(esserver, data=data)
d=response.json()
result = (d['hits']['hits'])
count=0
res=[]
mid=[]
for i in result:
	count+=1
	if count==11:
		res.append(mid)
		mid=[]
		count=0
	mid.append(i)

if count!=0:
	res.append(mid)

print(res)

