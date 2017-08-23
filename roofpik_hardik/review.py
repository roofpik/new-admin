from flask import request
from flask_restful import reqparse
from restful import Resource
import requests
import json

class ProjKeyRatings(Resource):

        def get(self):
                try:
                        parser = reqparse.RequestParser()
                        parser.add_argument('pkey', type=str, help='project key')
                        parser.add_argument('pagination', type=str, help='page number')
                        args = parser.parse_args()
                        pkey = args['pkey']
                        pagination = args['pagination']
                        query = {}
                        query['query'] = {}
                        query['query']['match'] = {}
                        '''_key = '-KYJONgh0P98xoyPPYm9' '''
                        query['query']['match']['project.city'] = pkey

                        if not pagination:
                                pstart = 0
                        else:
                                pstart = (int(pagination)-1)*10

                        items = []
                        esserver = 'https://search-roof-pnslfpvdk2valk5lfzveecww54.ap-south-1.es.amazonaws.com'
                        r = requests.get(esserver + '/allreviewsin/data/_search?size=10&from='+str(pstart), data=json.dumps(query))
                        result = json.loads(r.content)['hits']['hits']
                        res=[]

                        for i in range(0,len(result)):
                        	pname=result[i]['_source']['project']['name']
                        	uname=result[i]['_source']['user']['uname']
                        	mrating=result[i]['_source']['main']['rating']
                        	title=result[i]['_source']['main']['title']
                        	detail=result[i]['_source']['main']['detail']
                        	date=result[i]['_source']['main']['reviewDate']
                        	# print pname,uname,mrating,title,detail
                        	
                        	res.append({
                                        'pname':pname ,
                                        'uname': uname,
                                        'mrating':mrating,
                                        'title':title,
                                        'detail':detail,
                                        'reviewDate':date
                                        	
                                        
                                  })
                        return {'status':'200', 'items': res}
                except Exception as e:
                        return {'status':'400','Message':str(e)}