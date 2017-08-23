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
ptoken='CqQDkgEAAO-autdrrzLWN7vd1sSG3T1wIpyslc9I5Zs51JcYlhty1Pa07as8pgOAMUP6vbkMASE9zcpWD9grK3K7H8g9xO0Kx8cZ21JlQC6kQQpow4U1zc2mVROTkzSerqzGZ_vnOcIp09EqVUOHmzLtf_qp0wobXsu62zpJI87OCnqVKjOYsuoSBFy6c4g9QXHeGglIHIBL7lPVmsA12hBZDU5I0c3GbvmYMk5QPsiU2LeRddEGWnQdvdkeMo0vvBEqNpCld8K8HCLW22hPoQNRGa6Q9SKVMV8JqUbNGTty1ym_HSQiBaHR1ZvWKBqlsfgP1cTGcQyl5XG_K4bSasvN3EOS7ncPBWNI_YCH2j9uFsgg6jMCJvOwwS5HPBCijj08qXzqdoEsaXIeElBefWt5BWNZs79vQzLAtxTftST9aQzHime5cyq8jSetekkm7gykDMUGAAUZYluL8eCDy-_LQknB5bdlvWPSA8E2OOtnQOMOo9aQ_aL8SlAziyLQOCGGUH0l91AZRXzmwc7aDLr8D_bVv3rHg8ugJKHRDcKnDSvFfYleEhBVdsCDPtYUSI-8_knyoBVNGhRbqIcfPlvi4B1crcWtpaT5opNx7A'
#ptoken=''
count=0
url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=coworking+spaces+in+gurgaon&key=AIzaSyCfJt7vD0QNEdfky2lOH2Ghler5Zj_Gr2I&pagetoken='+str(ptoken)
r=requests.get(url)
k=r.json()
for i in range(0,len(k['results'])):
	l1.append(k['results'][i]['name'])
	l2.append(pcs(pcs(k['results'][i]['formatted_address'],', Gurugram, Haryana'),', India'))
	l3.append('gurgaon')
	l4.append('coworking')


'''url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=coworking+spaces+in+gurgaon&key=AIzaSyCfJt7vD0QNEdfky2lOH2Ghler5Zj_Gr2I&pagetoken='+str(jk)

r=requests.get(url)
k=r.json()
pprint(k)'''
df = DataFrame({'project Title': l1, 'Location': l2,'City': l3, 'Type': l4 })
df.to_excel('coworking3.xlsx', sheet_name='sheet1', index=False)




