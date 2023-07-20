# -*- coding: utf-8 -*-

from ...Serializer import Serializer

__all__ = (
	'Decoder'
)


class Decoder(Serializer):
	"""
	Decoder Class for Text
	"""

	def __call__(self, obj):
		if not isinstance(obj, str):
			raise RuntimeError('{} is not string'.format(obj))
		return obj
