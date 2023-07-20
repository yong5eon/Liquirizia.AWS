# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function.Implements.WebApplication import FunctionEventHandler

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

	def onRequest(self, request):
		print('REQUEST         : {}'.format(request))
		return

	def onRequestSuccess(self, request, response):
		print('REQUEST SUCCESS : {} - {}\n{}'.format(request, response, response.body.decode('utf-8')))
		return

	def onRequestError(self, request, error):
		print('REQUEST ERROR   : {} - {}'.format(request, str(error)), file=stderr)
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
