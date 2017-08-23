import json
import requests
from pprint import pprint
# transferring required data
'''
with open('data.json','r') as json_data:
	d=json.load(json_data)



with open('req_data.json', 'w') as outfile:  
    json.dump(d['reviews'], outfile,indent=4)'''

# finding redundant matrix for Cghs





'''with open('req_data.json','r') as json_data:
	d=json.load(json_data)

temp=d['-KYJONgh0P98xoyPPYm9']['cghs']
print len(temp)

st=set()
sum=0
for i in temp:
	for j in temp[i]:
		sum+=1
		for k in temp[i][j]['ratings'] :
			st.add(k)
		#print(' ------------------------------------------------------')
for i in temp:
	for j in temp[i]:
		for k in  temp[i][j]:
			if k!='ratings':
				st.add(k)


st1=sorted(st)
d=set()

for s in st1:
    print s


print('--------------------------------------------------------------------')

for i in temp:
	for j in temp[i]:
		for k in temp[i][j]:
			if k !='ratings':#['infrastructure','convenienceOfParking','openAndGreenAreas','convenienceOfHouseMaids','amenities','security']
				d.add((k,temp[i][j][k]))

print('--------------------------------------------------------------------')

for i in temp:
	for j in temp[i]:
		for k in temp[i][j]['ratings'] :
			d.add((k,temp[i][j]['ratings'][k]))

for s in sorted(d) :
	print s


print sum 
'''


# finding redundant matrix for Cghs


with open('req_data.json','r') as json_data:
	d=json.load(json_data)
temp=d['-KYJONgh0P98xoyPPYm9']['location']

'''for i in temp:
	for j in temp[i]:
		for k in temp[i][j]:
			print k
		print('-------------------------------------------------------')'''

st=set()
for i in temp:
	for j in temp[i]:
		for k in  temp[i][j]:
			st.add(k)


st1=sorted(st)
d=set()

for s in st1:
    print s

print('-------------------------------------------------------')

for i in temp:
	for j in temp[i]:
		for k in temp[i][j]:
			if k !='ratings':#['infrastructure','convenienceOfParking','openAndGreenAreas','convenienceOfHouseMaids','amenities','security']
				d.add((k,temp[i][j][k]))

print('--------------------------------------------------------------------')
for i in temp:
	for j in temp[i]:
		jk=temp[i][j]
		for k in jk:
			if k =='ratings':
				for l in jk['ratings']:
					d.add((l,jk['ratings'][l]))


for s in sorted(d) :
	print s