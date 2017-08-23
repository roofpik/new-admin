import requests
from bs4 import BeautifulSoup
import csv
import openpyxl
from pandas import DataFrame

def pcs(str1,str2):
	return str1.replace(str2,'')
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(1,5): 
	URL = "http://www.99acres.com/search/project/buy/residential/gurgaon?search_type=QS&search_location=SH&lstAcn=NPSEARCH&lstAcnId=7098017818436838&src=CLUSTER&preference=S&city=8&res_com=R&selected_tab=3&isvoicesearch=N&keyword_suggest=gurgaon%3B&fullSelectedSuggestions=gurgaon&strEntityMap=W3sidHlwZSI6ImNpdHkifSx7IjEiOlsiZ3VyZ2FvbiIsIkNJVFlfOCwgUFJFRkVSRU5DRV9TLCBSRVNDT01fUiJdfV0%3D&texttypedtillsuggestion=gurga&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&suggestion=CITY_8%2C%20PREFERENCE_S%2C%20RESCOM_R&searchform=1&price_min=null&price_max=null&page="+str(i)
	r = requests.get(URL)
	soup = BeautifulSoup(r.content, 'html5lib')
	for row in soup.findAll('a', attrs = {'class':'npt_titl_desc'}):
		str1=pcs(row.text.lower(),row.span.text.lower())
		str2=pcs(pcs(row.span.text.lower(),'gurgaon'),',')
		l1.append(str1)
		l2.append(str2)
		l3.append('gurgaon')
		l4.append('residential')

'''df = DataFrame({'Project Title': l1, 'Location': l2,'City': l3, 'Type': l4 })
df.to_excel('residential3.xlsx', sheet_name='sheet1', index=False)		'''

print len(l1)


#print links



