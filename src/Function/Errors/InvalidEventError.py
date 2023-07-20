# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'InvalidEventError'
)


class InvalidEventError(Error):
	"""
	Invalid Event Error for Event Broker
	"""
	def __init__(self, reason=None):
		super(InvalidEventError, self).__init__('Invalid Event Error{}'.format('({})'.format(reason) if reason else ''))
		return
