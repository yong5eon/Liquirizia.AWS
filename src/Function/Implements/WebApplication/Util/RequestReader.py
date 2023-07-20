# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import Request
from Liquirizia.WebApplication.Util import (
	ToQueryString,
	ToHeaderName,
)
from Liquirizia.WebApplication.Serializer import SerializerHelper
from base64 import b64decode

__all__ = (
	'Request'
)


class RequestReader(Request):
	"""
	Request Reader Class for Web Application Function Handler
	"""
	def __init__(self, event):
		# input format :
		#
		# {
		# 	"Records": [
		# 		{
		# 			"cf": {
		# 				"config": {
		# 					"distributionId": "EDFDVBD6EXAMPLE"
		# 				},
		# 				"request": {
		# 					"clientIp": "2001:0db8:85a3:0:0:8a2e:0370:7334",
		# 					"method": "GET",
		# 					"uri": "/picture.jpg",
		# 					"headers": {
		# 						"host": [
		# 							{
		# 								"key": "Host",
		# 								"value": "d111111abcdef8.cloudfront.net"
		# 							}
		# 						],
		# 						"user-agent": [
		# 							{
		# 								"key": "User-Agent",
		# 								"value": "curl/7.51.0"
		# 							}
		# 						]
		# 					}
		# 				}
		# 			}
		# 		}
		# 	]
		# }
		request = event['Records'][0]['cf']['request']
		super(RequestReader, self).__init__(
			method=request['method'],
			uri=request['uri'],
			version='HTTP/1.1',  # TODO : check if version is exist in request
		)
		for k, v in request['headers'].items() if 'headers' in request and request['headers'] else []:
			super(RequestReader, self).header(ToHeaderName(k), v[0]['value'])
		if 'clientIp' in request and request['clientIp']:
			super(RequestReader, self).header('X-Client-Ip-Address', request['clientIp'])
		return

