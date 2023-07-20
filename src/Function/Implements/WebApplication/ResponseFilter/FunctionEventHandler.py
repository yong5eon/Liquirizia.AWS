# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function import FunctionEventHandler as Base

from Liquirizia.WebApplication import (
	Response,
	Error,
)

__all__ = (
	'FunctionEventHandler'
)


class FunctionEventHandler(Base):
	"""
	Response Filter Function Event Handler Interface of Web Application
	"""
	def onResponseFilter(self, response: Response):
		raise NotImplementedError('{} must be implemented onResponseFilter'.format(self.__class__.__name__))

	def onResponseFilterSuccess(self, response: Response):
		raise NotImplementedError('{} must be implemented onResponseFiltered'.format(self.__class__.__name__))

	def onResponseFilterError(self, response: Response, error: Error):
		raise NotImplementedError('{} must be implemented onResponseFilterError'.format(self.__class__.__name__))
