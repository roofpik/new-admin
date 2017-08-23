import requests
from bs4 import BeautifulSoup
import csv
import openpyxl
from pandas import DataFrame

'''for i in range(1,11): 
	URL = "http://www.99acres.com/property-in-gurgaon-ffid?orig_property_type=23&search_type=QS&search_location=SH&lstacn=NPSEARCH&np_layout=xid_property_layout&page="+str(i)
	r = requests.get(URL)
	soup = BeautifulSoup(r.content, 'html5lib')
	for row in soup.findAll('span', attrs = {'class':'doElip'}):
		print row.text'''

URL = 'http://www.99acres.com/property-in-gurgaon-ffid?orig_property_type=23&search_type=QS&search_location=SH&lstacn=NPSEARCH&np_layout=xid_property_layout'
r=requests.get(URL)
soup = BeautifulSoup(r.content,'html5lib')
for row in soup.findAll('a',class_='sname'):
	print row.text

print soup.find('doElip')

