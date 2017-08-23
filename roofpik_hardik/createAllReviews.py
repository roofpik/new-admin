import requests
import json
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir+'/data') 
import alldata
import re


esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com/'
# esserver = 'http://localhost:9200/'


def genReviewsData():

	esobject = {}
	locationdata = alldata.data['locations']['country']['-K_43TEI8cBodNbwlKqJ']['locality']['city']['-KYJONgh0P98xoyPPYm9']['micromarket']
	micromarketdata = alldata.data['locations']['country']['-K_43TEI8cBodNbwlKqJ']['micromarket']['city']['-KYJONgh0P98xoyPPYm9']['places']
	allprojdata = alldata.data['project']['country']['-K_43TEI8cBodNbwlKqJ']['city']['-KYJONgh0P98xoyPPYm9']['residential']['micromarket']
	reviewdata = alldata.data['reviews']['project']['country']['-K_43TEI8cBodNbwlKqJ']['city']['-KYJONgh0P98xoyPPYm9']['residential']

	count = 0
	for projkey in reviewdata:
		# if projkey == '-K_nmquYqUx0JmvLavz-':
		projReviews = reviewdata[projkey]['reviews']
		for reviewKey in projReviews:
			count += 1
			createReviewsIn(projReviews[reviewKey])

				# print json.dumps(reviewdata[projkey]['reviews'], indent=4, separators=(',', ': '))

	print count
def createReviewsIn(data):
	payload = json.dumps(data)
	url = esserver + "allreviewsin/data/" + data['main']['key']
	r = requests.put(url, data=payload)


genReviewsData()