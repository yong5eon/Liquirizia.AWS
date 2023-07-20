# -*- coding: utf-8 -*-

from collections import MutableSequence, MutableMapping, MutableSet
from datetime import datetime, date
from decimal import Decimal
from json import dumps, JSONEncoder

from ...Serializer import Serializer

__all__ = (
	'Encoder'
)


class TypeEncoder(JSONEncoder):
	"""
	Type Encoder for JSON
	"""

	def default(self, obj):
		if isinstance(obj, Decimal):
			return float(obj)
		if isinstance(obj, MutableSequence):
			return list(obj)
		if isinstance(obj, MutableMapping):
			return dict(obj)
		if isinstance(obj, MutableSet):
			return tuple(obj)
		if isinstance(obj, (date, datetime)):
			return obj.isoformat()
		return None


class Encoder(Serializer):
	"""
	Encoder Class for JSON
	"""

	def __call__(self, obj):
		return dumps(obj, ensure_ascii=False, cls=TypeEncoder)
	
	
