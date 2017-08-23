from flask import request
from restful import Resource
from flask_restful import reqparse
import requests
import json

class merge_reviews(Resource):
	

	def get(self):
		try:
			def greviews(pid):
				url='https://maps.googleapis.com/maps/api/place/details/json?placeid='+pid+'&key=AIzaSyC49HojGuiH2hda1KH7DXo15epl-FQ--2M'
				r=requests.get(url)
				res=r.json()
				return res

			def lreviews(name):
				url='http://localhost:80/v1/nameSearch?pname='+name
				r=requests.get(url)
				res=[]
				res=r.json()['items']
				return res

			parser = reqparse.RequestParser()
			parser.add_argument('pname', type=str, help='project name')
			parser.add_argument('pid', type=str, help='place id')
			args = parser.parse_args()
			name=args['pname']
			pid=args['pid']
			tmp=greviews(pid)
			name=tmp['result']['name']
			addr=tmp['result']['formatted_address']
			loc=tmp['result']['geometry']['location']
			gres=tmp['result']['reviews']
			lres=[]
			lres=lreviews(name)
			res={'name':name,'address':addr,'location':loc,'id':pid,'gres':gres,'lres':lres }
			return {'status':'200', 'items': res}

		except Exception as e:
			return {'status':'400','Message':str(e)}

