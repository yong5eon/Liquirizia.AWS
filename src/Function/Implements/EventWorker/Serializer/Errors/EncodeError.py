# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'EncodeError'
)


class EncodeError(Error):
	def __init__(self, value, format=None, charset=None, error=None):
		super(EncodeError, self).__init__('{} can not encoded{}{}'.format(value, ' with {}'.format(format) if format else '', ', charset={}'.format(charset) if charset else ''), error=error)
		return
