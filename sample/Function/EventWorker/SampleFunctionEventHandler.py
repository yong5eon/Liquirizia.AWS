# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function.Implements.EventWorker import FunctionEventHandler

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

	def onRequest(self, event: str, headers: dict = None, body=None):
		print('REQUEST         : {}, {}, {}'.format(event, headers, body))
		return

	def onRequestSuccess(self, event: str, headers: dict = None, body=None, res=None):
		print('REQUEST SUCCESS : {}'.format(res))
		return

	def onRequestError(self, event: str, headers: dict = None, body=None, error=None):
		print('REQUEST ERROR   : {}'.format(str(error)), file=stderr)
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
