# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import Request
from Liquirizia.WebApplication.Util import (
	ToHeaderName,
)

from abc import ABCMeta
from collections import MutableMapping

_all__ = (
	'RequestWriter'
)


class Meta(ABCMeta):
	def __new__(mcls, name, bases, namespace, *, realbase=dict, **kwargs):
		abc_cls = super().__new__(mcls, name, bases, namespace, **kwargs)
		for attr_name in dir(abc_cls):
			attr = getattr(abc_cls, attr_name)
			if getattr(attr, "__module__", None) == "collections.abc" and attr_name not in namespace:
				namespace[attr_name] = attr
		return type.__new__(mcls, name, (realbase,), namespace)


class RequestWriter(MutableMapping, metaclass=Meta):
	"""
	Response Writer Class for Web Application Function Handler
	"""
	def __init__(self, request: Request):
		# output format :
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
		self.properties = {
			'clientIp': request.header('X-Client-Ip-Address'),
			'method': request.method,
			'uri': request.uri,
			'headers': {ToHeaderName(header[0]): [{ToHeaderName(header[0]): header[1]}] for header in request.headers()},
		}
		return

	def __repr__(self):
		return repr(self.properties)

	def __getitem__(self, key):
		return self.properties.__getitem__(key)

	def __setitem__(self, key, value):
		self.properties.__setitem__(key, value)

	def __delitem__(self, key):
		self.properties.__delitem__(key)
		return

	def __len__(self):
		return len(self.properties)

	def __iter__(self):
		return iter(self.properties)

	def __contains__(self, key):
		return key in self.properties

	def __copy__(self):
		return dict(self.properties)

	def __deepcopy__(self, memo):
		return dict(self.properties)

	def keys(self):
		return self.properties.keys()

	def items(self):
		return self.properties.items()
