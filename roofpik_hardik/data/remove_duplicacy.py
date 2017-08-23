import json
from sets import Set
from pprint import pprint
with open('data.json') as json_data:
    d = json.load(json_data)
    #pprint(d)
temp=d['reviews']['project']['country']#['-K_43TEI8cBodNbwlKqJ']['city']['-KYJONgh0P98xoyPPYm9']['residential']#['-KYMt4pSYjIUsknqZ6Qr']['reviews']
'''for i in temp:
	print temp[i]['user']['uname']'''
count=0
global_list=[]
my_set=Set()
my_set1=Set()
my_list=[]
my_list1=[]
for i in temp:
	helper=temp[i]['city']
	for j in helper:
		temp1=helper[j]['residential']
		for k in temp1:
			temp2=temp1[k]['reviews']
			for l in temp2:
				lent=len(my_set)
				my_set.add(temp2[l]['user']['uname'])
				if lent==len(my_set) :
					global_list.append(temp2[l]['user']['uname'])
					with open('data_repeated.txt', 'a') as outfile:
						outfile.write(str(temp2[l]['user']['uname'])+'\n')
						outfile.close()


				if temp2[l]['user']['mobile']!=False :
					my_set1.add(temp2[l]['user']['mobile'])
				my_list.append(temp2[l]['user']['uname'])
				if temp2[l]['user']['mobile']!=False :
					my_list1.append(temp2[l]['user']['mobile'])

				count+=1

print count # total number of data
print len(my_set) # no . of unique names
print len(my_set1) # no .of unique phone numbers not false
print len(my_list) # total number of names
print len(my_list1) # total number of phone numbers not false
pprint(global_list) # all the resultant json 
