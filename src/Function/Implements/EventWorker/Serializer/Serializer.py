# -*- coding: utf-8 -*-

__all__ = (
	'Serializer'
)


class Serializer(object):
	"""
	Serializer Interface Class
	"""
	def __call__(self, obj):
		raise NotImplementedError('Serializer must be implemented __call__, constructor method')
