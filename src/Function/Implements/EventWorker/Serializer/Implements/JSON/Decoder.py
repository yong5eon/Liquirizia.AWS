# -*- coding: utf-8 -*-

from json import loads, JSONDecoder
from datetime import date, datetime

from ...Serializer import Serializer

__all__ = (
	'Decoder'
)


class TypeDecoder(JSONDecoder):
	"""
	Type Decoder for JSON
	"""
	
	def __init__(self, *args, **kwargs):
		super(TypeDecoder, self).__init__(object_hook=self.any, *args, **kwargs)
		return
	
	def any(self, obj):
		if isinstance(obj, dict):
			for key, value in obj.items():
				if isinstance(value, str):
					try:
						obj[key] = date.fromisoformat(value)
						continue
					except:
						pass
					try:
						obj[key] = datetime.fromisoformat(value)
						continue
					except:
						pass
				elif isinstance(value, (list, tuple)):
					for i, v in enumerate(value):
						if isinstance(v, str):
							try:
								value[i] = date.fromisoformat(v)
								continue
							except:
								pass
							try:
								value[i] = datetime.fromisoformat(v)
								continue
							except:
								pass
		return obj
	

class Decoder(Serializer):
	"""
	Decoder Class for JSON
	"""
	
	def __call__(self, obj):
		if not isinstance(obj, str):
			raise RuntimeError('{} is not string'.format(obj))
		return loads(obj, cls=TypeDecoder)
	
	
