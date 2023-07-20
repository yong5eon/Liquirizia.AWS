# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import Response
from Liquirizia.WebApplication.Util import (
	ToHeaderName,
)
from Liquirizia.WebApplication.Serializer import SerializerHelper
from base64 import b64decode

__all__ = (
	'ResponseReader'
)


class ResponseReader(Response):
	"""
	Response Reader Class for Web Application Function Handler
	"""
	def __init__(self, response):
		# input format :
		#
		# {
		# 	'status': '200',
		# 	'statusDescription': 'OK',
		# 	'headers': {
		# 		'cache-control': [
		# 			{
		# 				'key': 'Cache-Control',
		# 				'value': 'max-age=100'
		# 			}
		# 		],
		# 		"content-type": [
		# 			{
		# 				'key': 'Content-Type',
		# 				'value': 'text/html'
		# 			}
		# 		]
		# 	},
		# 	'body': CONTENT
		# }
		super(ResponseReader, self).__init__(
			status=int(response['status']),
			message=response['statusDescription'],
			version='HTTP/1.1',  # TODO : check if version is exist in request
			body=response['body']
		)
		for k, v in response['headers'].items() if 'headers' in response and response['headers'] else []:
			super(ResponseReader, self).header(ToHeaderName(k), v[0]['value'])
		return
