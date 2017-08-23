import json
import requests
from sets import Set
from pprint import pprint

def location_migrator():
	with open('data.json') as json_data:
		d = json.load(json_data)
	temp=d['reviews']['project']['country']
	pprint(temp)

location_migrator()