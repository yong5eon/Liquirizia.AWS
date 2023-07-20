# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'DecodeError'
)


class DecodeError(Error):
	def __init__(self, value, format=None, charset=None, error=None):
		super(DecodeError, self).__init__('{} can not decoded{}{}'.format(value, ' with {}'.format(format) if format else '', ', charset={}'.format(charset) if charset else ''), error=error)
		return
