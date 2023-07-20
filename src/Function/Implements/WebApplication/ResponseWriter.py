# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import Response
from Liquirizia.WebApplication.Util import (
	HeadersToMap,
)

from abc import ABCMeta
from collections import MutableMapping
from base64 import b64encode

_all__ = (
	'ResponseWriter'
)


class Meta(ABCMeta):
	def __new__(mcls, name, bases, namespace, *, realbase=dict, **kwargs):
		abc_cls = super().__new__(mcls, name, bases, namespace, **kwargs)
		for attr_name in dir(abc_cls):
			attr = getattr(abc_cls, attr_name)
			if getattr(attr, "__module__", None) == "collections.abc" and attr_name not in namespace:
				namespace[attr_name] = attr
		return type.__new__(mcls, name, (realbase,), namespace)


class ResponseWriter(MutableMapping, metaclass=Meta):
	"""
	Response Writer Class for Web Application Function Handler
	"""
	def __init__(self, response: Response):
		# output format :
		#
		# {
		#     "isBase64Encoded": true|false,
		#     "statusCode": httpStatusCode,
		#     "headers": { "headerName": "headerValue", ... },
		#     "multiValueHeaders": { "headerName": ["headerValue", "headerValue2", ...], ... },
		#     "body": "..."
		# }
		#
		self.properties = {
			'statusCode': response.status,
			'headers': HeadersToMap(response.headers()),
			'isBase64Encoded': True,
			'body': b64encode(response.body) if response.body else None
		}
		pass

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
