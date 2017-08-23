import requests
import json
from pprint import pprint

def greviews(pid):
	
	url='https://maps.googleapis.com/maps/api/place/details/json?placeid='+pid+'&key=AIzaSyC49HojGuiH2hda1KH7DXo15epl-FQ--2M'
	r=requests.get(url)
	res=r.json()
	return res



def lreviews(name):
	
	url='http://localhost:80/v1/nameSearch?pname='+name
	r=requests.get(url)
	res=[]
	res=r.json()['items']
	return res


def combined():
	pid='ChIJfx7J9cQYDTkRFYpijt8cZqA'
	name='DLF Regent House'
	tmp=greviews(pid)
	name=tmp['result']['name']
	addr=tmp['result']['formatted_address']
	loc=tmp['result']['geometry']['location']
	gres=tmp['result']['reviews']
	lres=[]
	lres=lreviews(name)


	return ({'name':name,'address':addr,'location':loc,'id':pid,'gres':gres,'lres':lres })

pprint(combined())


