# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function.Implements.WebApplication.ResponseFilter import FunctionEventHandler

from Liquirizia.WebApplication import Response, Error

from sys import stderr

__all__ = (
	'SampleFunctionEventHandler'
)


class SampleFunctionEventHandler(FunctionEventHandler):
	def onInitialize(self):
		print('INITIALIZE')
		return

	def onEventRequest(self, name, version, arn, limit, timeout, tag=None):
		print('EVENT REQUEST   : {}, {}, {}, {}, {}, {}'.format(
			name,
			version,
			arn,
			limit,
			timeout,
			tag
		))

	def onEvent(self, event):
		print('EVENT           : {}'.format(event))
		return

	def onResponseFilter(self, response):
		print('FILTER          : {}'.format(response))
		return

	def onResponseFilterSuccess(self, response: Response):
		print('FILTER  SUCCESS : {}'.format(response))
		return

	def onResponseFilterError(self, response, error: Error):
		print('FILTER  ERROR   : {} - {}'.format(response, str(error)), file=stderr)
		return

	def onEventSuccess(self, event, res=None):
		print('EVENT SUCCESS   : {} - {}'.format(event, str(res) if res else ''))
		return

	def onEventError(self, event, error=None):
		print('EVENT ERROR     : \n{}\n{}'.format(event, str(error) if error else ''), file=stderr)
		return

	def onRelease(self):
		print('RELEASE')
		return
