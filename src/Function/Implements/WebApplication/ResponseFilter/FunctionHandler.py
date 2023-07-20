# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function import FunctionHandler as Base

from Liquirizia.WebApplication import (
	ResponseFilter,
	Error
)

from .FunctionEventHandler import FunctionEventHandler
from ..Util import (
	ResponseReader,
	ResponseWriter,
)

__all__ = (
	'FunctionHandler'
)


class FunctionHandler(Base):
	"""
	Response Filter Function Handler Class of Web Application
	"""
	def __init__(
		self,
		handler: FunctionEventHandler,
		fn: ResponseFilter,
	):
		super(FunctionHandler, self).__init__(handler)
		self.handler = handler
		self.filter = fn
		return

	def run(self, event):
		response = None
		try:
			response = ResponseReader(event)
			self.handler.onResponseFilter(response)
			response = self.filter.run(response)
			self.handler.onResponseFilterSuccess(response)
			return ResponseWriter(response)
		except Error as e:
			self.handler.onResponseFilterError(response, error=e)
			raise e
