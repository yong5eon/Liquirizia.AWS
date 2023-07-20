# -*- coding: utf-8 -*-

from Liquirizia.EventRunner import EventRunnerComplete

__all__ = (
	'SampleEventRunnerComplete'
)


class SampleEventRunnerComplete(EventRunnerComplete):
	def __call__(self, event, headers=None, body=None, res=None):
		print('COMPLETE : {}'.format(res))
		return
