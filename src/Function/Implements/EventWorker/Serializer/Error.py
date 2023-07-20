# -*- coding: utf-8 -*-

import traceback

__all__ = (
	'Error'
)


class Error(BaseException):
	"""
	Error for Event Broker Serializer
	"""
	def __init__(self, reason, error=None):
		super(Error, self).__init__(reason)
		self.reason = reason
		self.error = error
		return

	def __repr__(self):
		return '{}{}'.format(
			self.reason,
			' - {}'.format(str(self.error)) if self.error else '',
		)

	def __str__(self):
		reason = '{}{}'.format(
			self.reason,
			' - {}'.format(str(self.error)) if self.error else '',
		)
		if self.error:
			reason += '\n'
			for line in ''.join(traceback.format_tb(self.error.__traceback__)).strip().split('\n'):
				reason += line + '\n'
		return reason
