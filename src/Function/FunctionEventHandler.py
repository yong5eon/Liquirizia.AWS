# -*- coding: utf-8 -*-

__all__ = (
	'FunctionEventHandler'
)


class FunctionEventHandler(object):
	"""
	Function Event Handler Interface

	Sample:
	class MyFunctionEventHandler(FunctionEventHandler):
		def onInitialized(self, *args, **kwargs):
			...
			return
		def onInvoked(self, event, context):
			...
			return
		def onError(self, event, context, error):
			...
			return
		def onDestroy(self):
			...
			return
	"""
	def onInitialize(self):
		raise NotImplementedError('{} must be implemented onInitialize'.format(self.__class__.__name__))

	def onEventRequest(self, name, version, arn, limit, timeout, tag=None):
		raise NotImplementedError('{} must be implemented onEvent'.format(self.__class__.__name__))

	def onEvent(self, event):
		raise NotImplementedError('{} must be implemented onEvent'.format(self.__class__.__name__))

	def onEventSuccess(self, event, res=None):
		raise NotImplementedError('{} must be implemented onEventSuccess'.format(self.__class__.__name__))

	def onEventError(self, event, error: BaseException = None):
		raise NotImplementedError('{} must be implemented onEventError'.format(self.__class__.__name__))

	def onRelease(self):
		raise NotImplementedError('{} must be implemented onRelease'.format(self.__class__.__name__))

