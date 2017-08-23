import requests
from bs4 import BeautifulSoup
import csv
import openpyxl
from pandas import DataFrame
import json
from pprint import pprint

with open('residential.json','r') as data:
	d=json.load(data)

res={}
count=0
for i in range(0,len(d)):
	count+=1
	name=str(d[i]['Project Title'])
	loc=str(d[i]['Project Title'])+' '+str(d[i]['Location'])+' '+str(d[i]['City'])
	url='https://maps.googleapis.com/maps/api/place/textsearch/json?query='+loc+'&key=AIzaSyCfJt7vD0QNEdfky2lOH2Ghler5Zj_Gr2I'
	r=requests.get(url).json()
	#k=r['results'][0]['place_id']
	print r
	#res[k]={'name': name, 'type' : 'residential' ,'location' : loc }
	if count==100:
		break


with open('result1.json', 'w') as outfile:  
    json.dump(res, outfile,indent=4)


