import json
import requests
from pprint import pprint

with open('data.json') as json_data:
	d=json.load(json_data)

temp=d['projects']['-KYJONgh0P98xoyPPYm9']['cghs']
#pprint(temp)
res={}
jk=True
for i in temp:	
	res[i]={}		
	res[i]['propertyTypes']={"penthouse": "NA", "rowhouse": "NA", "apartment": "NA", "villa": "NA"}
	res[i]['scores']={"affordable": "NA", "petFriendly": "NA", "ultraLuxury": "NA", "seniorLiving": "NA", "downtown": "NA", "bachelors": "NA", "luxury": "NA", "bestAmenities": "NA"}
	res[i]['status']={"basic": True, "meta": True, "amenities": True, "scores": False, "units": True, "spec": True}
	res[i]['active']=True
	res[i]['cover-image']=temp[i]['images']['coverPhoto']['url']
	res[i]['created']=1490529141175
	res[i]['updated']=1491886245909
	res[i]['key']=i
	res[i]['specifications']={}
	res[i]['specifications']['general']=temp[i]['specifications']
	res[i]['specifications']['fittings']={"toilets": "NA", "kitchen": "NA"}
	res[i]['specifications']['flooring']={"toilets": "NA", "masterBedroom": "NA", "livingDining": "NA", "otherBedroom": "NA", "kitchen": "NA"}
	res[i]['specifications']['windows']={"all": "NA"}
	res[i]['specifications']['walls']={"interior": "NA", "toilets": "NA", "exterior": "NA", "kitchen": "NA"}
	res[i]['specifications']['doors']={"main": "NA", "internal": "NA"}
	res[i]['highlights']={"pros": "NA","cons": "NA"}
	res[i]['name']=temp[i]['projectName']
	res[i]['locality']=temp[i]['projectDetails']['address']['localities']['primary']['localityId']
	res[i]['thumbnail']="NA"
	res[i]['micromarket']="NA"
	res[i]['meta']={}
	res[i]['meta']['keywords']=temp[i]['projectDetails']['address']['locations']['primary']['locationName']
	res[i]['meta']['description']="NA"
	res[i]['meta']['title']=temp[i]['projectName']
	res[i]['general']={}
	res[i]['general']['website']=temp[i]['projectDetails']['officialWebsite']
	res[i]['general']['about']="NA"
	res[i]['general']['power']="NA"
	res[i]['general']['builder']="CGHS"
	res[i]['general']['floors']=temp[i]['projectDetails']['floors']['max']
	res[i]['general']['rent']=temp[i]['price']['rent']['min']
	res[i]['general']['maintenance']="NA"
	res[i]['general']['units']=temp[i]['projectDetails']['numberOfUnits']
	res[i]['general']['security']="24x7"
	res[i]['general']['segment']=temp[i]['segment']
	res[i]['general']['tower']=temp[i]['projectDetails']['numberOfTowers']
	res[i]['general']['yop']="NA"
	res[i]['images']="NA"
	res[i]['location']={}
	res[i]['location']['addline1']=temp[i]['projectDetails']['address']['addressLine1']
	res[i]['location']['city']=temp[i]['projectDetails']['address']['cityName']
	res[i]['location']['addline2']=temp[i]['projectDetails']['address']['addressLine2']
	res[i]['location']['pincode']=temp[i]['projectDetails']['address']['pincode']
	res[i]['location']['displayAdd']=temp[i]['projectDetails']['address']['displayAddress']
	res[i]['location']['lat']=temp[i]['projectDetails']['address']['lat']
	res[i]['location']['lng']=temp[i]['projectDetails']['address']['lng']
	for j in temp[i]:
		if j=='amenities':
			res[i][j]=temp[i][j]
		if j=='configurations':
			res[i]['units']={}
			for k in temp[i][j]:
				res[i]['units'][k]={}
				res[i]['units'][k]['poojaRoom']=temp[i][j][k]['poojaRoom']
				res[i]['units'][k]['bathroom']=temp[i][j][k]['bathroom']
				res[i]['units'][k]['area']=temp[i][j][k]['superBuiltArea']
				res[i]['units'][k]['bhk']=temp[i][j][k]['bhk']
				res[i]['units'][k]['servantRoom']=temp[i][j][k]['servantRoom']
				res[i]['units'][k]['rent']=temp[i][j][k]['pricing']['rent']['min']
				res[i]['units'][k]['key']=k
				res[i]['units'][k]['bedroom']="NA"
				res[i]['units'][k]['studyRoom']=temp[i][j][k]['studyRoom']
				res[i]['units'][k]['type']=temp[i][j][k]['unit']


with open('converted.json', 'w') as outfile:  
    json.dump(res, outfile,indent=4)
        








