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
	Web Application Function Event Handler Interface
	"""
	def onRequest(self, request: Request):
		raise NotImplementedError('{} must be implemented onRequest'.format(self.__class__.__name__))

	def onRequestSuccess(self, request: Request, response: Response):
		raise NotImplementedError('{} must be implemented onRequestSuccess'.format(self.__class__.__name__))

	def onRequestError(self, request: Request, error: Error):
		raise NotImplementedError('{} must be implemented onRequestError'.format(self.__class__.__name__))
