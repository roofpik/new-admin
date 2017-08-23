import json
import requests
from pprint import pprint

with open('req_data1.json') as json_data:
	d=json.load(json_data)

with open('res1.json', 'w') as outfile:  
    json.dump(d, outfile,indent=4)