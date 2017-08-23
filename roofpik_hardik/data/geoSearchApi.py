from flask import request
from restful import Resource
from flask_restful import reqparse
import requests
import json

def geoSearchApi(Resource):
	def post(self):
			try:
				parser = reqparse.RequestParser()
				parser.add_argument('lat', type=str, help='Latitude point')
				parser.add_argument('lon', type=str, help='Longitude point')
				args = parser.parse_args()
				lat=args['lat']
				lon=args['lon']
				esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com/distance_search/location/_search?'
				data='{"query": {"bool": {"must": { "match_all": {}},"filter": {"geo_distance": {"distance": "10km","pin.location": {"lat":'+ str(lat)+',"lon":'+ str(lon)+'}}}}}}'
				response = requests.get(esserver, data=data)
				d=response.json()
				result = (d['hits']['hits'])



				return {'status':'200', 'items': result}
			except Exception as e:
				return {'status':'400','Message':str(e)}
