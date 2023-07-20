# -*- coding: utf-8 -*-

from ...Serializer import Serializer

__all__ = (
	'Encoder'
)


class Encoder(Serializer):
	"""
	Encoder Class for Text
	"""

	def __call__(self, obj):
		if not isinstance(obj, str):
			raise RuntimeError('{} is not string'.format(obj))
		return str(obj)
