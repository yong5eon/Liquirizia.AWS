# -*- coding: utf-8 -*-

from Liquirizia.EventRunner import EventRunnerError

__all__ = (
	'SampleEventRunnerError'
)


class SampleEventRunnerError(EventRunnerError):
	def __call__(self, event, headers=None, body=None, error=None):
		print('ERROR :')
		print(error)
		return
