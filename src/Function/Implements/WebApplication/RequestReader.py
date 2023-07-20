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
		#     "resource": "Resource path",
		#     "path": "Path parameter",
		#     "httpMethod": "Incoming request's method name"
		#     "headers": {String containing incoming request headers}
		#     "multiValueHeaders": {List of strings containing incoming request headers}
		#     "queryStringParameters": {query string parameters }
		#     "multiValueQueryStringParameters": {List of query string parameters}
		#     "pathParameters":  {path parameters}
		#     "stageVariables": {Applicable stage variables}
		#     "requestContext": {Request context, including authorizer-returned key-value pairs}
		#     "body": "A JSON string of the request payload."
		#     "isBase64Encoded": "A boolean flag to indicate if the applicable request payload is Base64-encode"
		# }
		#
		super(RequestReader, self).__init__(
			method=event['httpMethod'],
			uri='{}{}'.format(
				event['path'],
				'?{}'.format(ToQueryString(event['queryStringParameters'])) if event['queryStringParameters'] else ''
			),
			version=event['requestContext']['protocol']
		)

		for k, v in event['headers'].items() if 'headers' in event and event['headers'] else []:
			super(RequestReader, self).header(ToHeaderName(k), v)

		if 'body' in event and event['body']:
			if 'isBase64Encoded' in event and event['isBase64Encoded']:
				self.body = SerializerHelper.Decode(
					b64decode(event['body']),
					format=super(RequestReader, self).format,
					charset=super(RequestReader, self).charset,
				)
			else:
				self.body = event['body']

		return

