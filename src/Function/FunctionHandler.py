# -*- coding: utf-8 -*-

from .FunctionEventHandler import FunctionEventHandler

__all__ = (
	'FunctionHandler'
)


class FunctionHandler(object):
	"""
	Function Handler Abstract Class

	Sample:
	class MyFunctionHandler(FunctionHandler):
		def __init__(self, handler: FunctionEventHandler, *args, **kwargs):
			...
			return
		def __del__(self):
			...
			return
		def __call__(self, event, context):
			...
			return
	"""
	def __init__(self, handler: FunctionEventHandler):
		self.handler = handler
		self.handler.onInitialize()
		return

	def __del__(self):
		self.handler.onRelease()
		return

	def __call__(self, event, context):
		try:
			# ARN :
			#   arn:partition:service:region:account-id:resource-id:tag
			#   arn:partition:service:region:account-id:resource-type/resource-id:tag
			#   arn:partition:service:region:account-id:resource-type:resource-id:tag
			if context:
				arn = context.invoked_function_arn.split(':|/')
				self.handler.onEventRequest(
					context.function_name,
					context.function_version,
					':'.join(arn[:6]),
					context.memory_limit_in_mb,
					context.get_remaining_time_in_millis(),
					tag=arn[7] if len(arn) > 7 else None
				)
			else:
				self.handler.onEventRequest(
					None,
					None,
					None,
					None,
					None,
					None,
				)
			self.handler.onEvent(event)
			res = self.run(event)
			self.handler.onEventSuccess(event, res)
			return res
		except BaseException as e:
			self.handler.onEventError(event, error=e)
			raise e

	def run(self, event):
		raise NotImplementedError('{} must be implemented run to run function'.format(self.__class__.__name__))
