# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function.Implements.WebApplication.RequestFilter import FunctionEventHandler

from Liquirizia.WebApplication import Request, Response, Error

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

	def onRequestFilter(self, request):
		print('FILTER          : {}'.format(request))
		return

	def onRequestFilterSuccess(self, request: Request, response: Response):
		print('FILTER  SUCCESS : {}'.format(request))
		if response:
			print('\n{}\n{}'.format(response, response.body.decode('utf-8')))
		return

	def onRequestFilterError(self, request, error: Error):
		print('FILTER  ERROR   : {} - {}'.format(request, str(error)), file=stderr)
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
