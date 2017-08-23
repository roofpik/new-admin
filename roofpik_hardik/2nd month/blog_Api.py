from flask import request
from restful import Resource
from flask_restful import reqparse
import requests
import json


def blog_Api(Resource):
	def get(self):
		try:
			esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com/my_index2/data/_search'
			data='{"sort": { "updated": "desc"} }'
			response = requests.get(esserver, data=data)
			d=response.json()
			result = (d['hits']['hits'])
			count=0
			res=[]
			mid=[]
			for i in result:
				count+=1
				if count==11:
					res.append(mid)
					mid=[]
					count=0
				mid.append(i)
			if count!=0:
				res.append(mid)


			return {'status':'200', 'items': result}
		except Exception as e:
			return {'status':'400','Message':str(e)}