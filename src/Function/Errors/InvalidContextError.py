# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'InvalidContextError'
)


class InvalidContextError(Error):
	"""
	Invalid Context Error for Context Broker
	"""
	def __init__(self, reason=None):
		super(InvalidContextError, self).__init__('Invalid Context Error{}'.format('({})'.format(reason) if reason else ''))
		return
