from flask import request
from restful import Resource
from flask_restful import reqparse
import requests
import json

class propTypeApi(Resource):
        def post(self):
                try:
                        parser = reqparse.RequestParser()
                        parser.add_argument('rkey', type=str, help='random key')
                        parser.add_argument('rtype', type=str, help='random type')
                        args = parser.parse_args()
                        rkey = args['rkey']
                        rtype= args['rtype']
                        query = {}
                        query['query'] = {}
                        query['query']['match'] = {}
                        query['from'] = 0
                        query['size'] = 400
                        if rtype=='city':
                        	query['query']['match']['location.citykey'] = rkey
                        if rtype=='micromarket':
                        	query['query']['match']['location.microkey'] = rkey
                        if rtype=='locality':
                        	query['query']['match']['location.lockey'] = rkey


                        esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com'
                        r = requests.get(esserver + '/projectnewin_v1/data/_search?', data=json.dumps(query))
                        result = json.loads(r.content)['hits']['hits']





                        count_apart=0
                        count_villa=0
                        count_row=0
                        count_pent=0
                        for i in range(0,len(result)):
                                temp=result[i]['_source']['propType']
                                for j in temp:
                                        if j=='apartment':
                                                if temp[j]== True:
                                                        count_apart+=1
                                        if j=='villa':
                                                if temp[j]== True:
                                                        count_villa+=1
                                        if j=='penthouse':
                                                if temp[j]== True:
                                                        count_pent+=1                                   
                                        if j=='rowhouse':
                                                if temp[j]== True:
                                                        count_row+=1

                        res=[]
                        res.append({
                                        'apartment': count_apart,
                                        'villa': count_villa,
                                        'penthouse': count_pent,
                                        'rowhouse': count_row

                                })


                        return {'status':'200', 'items': res}
                except Exception as e:
                        return {'status':'400','Message':str(e)}
