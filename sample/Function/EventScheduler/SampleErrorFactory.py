# -*- coding: utf-8 -*-

from Liquirizia.Validator import Error

__all__ = (
	'SampleErrorFactory'
)


class SampleErrorFactory(Error):
	def __init__(self, reason, error):
		self.reason = reason
		self.error = error
		return

	def __call__(self, parameters, *args, **kwargs):
		return self.error(self.reason)
