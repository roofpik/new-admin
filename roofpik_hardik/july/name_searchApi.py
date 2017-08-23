from flask import request
from restful import Resource
from flask_restful import reqparse
import requests
import json

class name_searchApi(Resource):
	def get(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('pname', type=str, help='project name')
			args = parser.parse_args()
			pname=args['pname']
			query = {}
			query['query'] = {}
			query['query']['match_phrase'] = {}
			query['query']['match_phrase']['project.name'] = pname
			query['from'] = 0
			query['size'] = 2000

			esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com'
			r = requests.get(esserver + '/allreviewsin/data/_search?', data=json.dumps(query))
			result = json.loads(r.content)['hits']['hits']

			res=[]
			for i in range(0,len(result)):
				project=result[i]['_source']['project']
				user=result[i]['_source']['user']
				main=result[i]['_source']['main']
				res.append({'project':project,'user':user,'main':main})

			return {'status':'200', 'items': res}

		except Exception as e:
			return {'status':'400','Message':str(e)}
	
