# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function import FunctionHandler as Base

from Liquirizia.WebApplication import (
	RequestFilter,
	Error
)

from .FunctionEventHandler import FunctionEventHandler
from ..Util import (
	RequestReader,
	RequestWriter,
	ResponseWriter,
)

__all__ = (
	'FunctionHandler'
)


class FunctionHandler(Base):
	"""
	Request Filter Function Handler Class of Web Application
	"""
	def __init__(
		self,
		handler: FunctionEventHandler,
		fn: RequestFilter,
	):
		super(FunctionHandler, self).__init__(handler)
		self.handler = handler
		self.filter = fn
		return

	def run(self, event):
		request = None
		try:
			request = RequestReader(event)
			self.handler.onRequestFilter(request)
			request, response = self.filter.run(request)
			self.handler.onRequestFilterSuccess(request, response)
			if response:
				return ResponseWriter(response)
			return RequestWriter(request)
		except Error as e:
			self.handler.onRequestFilterError(request, error=e)
			raise e
