# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function import FunctionEventHandler as Base

from Liquirizia.WebApplication import (
	Request,
	Response,
	Error,
)

__all__ = (
	'FunctionEventHandler'
)


class FunctionEventHandler(Base):
	"""
	Request Filter Function Event Handler Interface of Web Application
	"""
	def onRequestFilter(self, request: Request):
		raise NotImplementedError('{} must be implemented onRequestFilter'.format(self.__class__.__name__))

	def onRequestFilterSuccess(self, request: Request, response: Response):
		raise NotImplementedError('{} must be implemented onRequestFiltered'.format(self.__class__.__name__))

	def onRequestFilterError(self, request: Request, error: Error):
		raise NotImplementedError('{} must be implemented onRequestFilterError'.format(self.__class__.__name__))
