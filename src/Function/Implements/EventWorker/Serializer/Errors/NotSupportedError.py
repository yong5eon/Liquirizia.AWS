# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'NotSupportedError'
)


class NotSupportedError(Error):
	def __init__(self, format):
		super(NotSupportedError, self).__init__('{} is not supported type in Serializer'.format(format))
		return
