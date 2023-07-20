# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function import FunctionEventHandler as Base

__all__ = (
	'FunctionEventHandler'
)


class FunctionEventHandler(Base):
	"""
	Event Worker Function Event Handler Interface
	"""
	def onRequest(self, event: str, headers: dict = None, body=None):
		raise NotImplementedError('{} must be implemented onEvent'.format(self.__class__.__name__))

	def onRequestSuccess(self, event: str, headers: dict = None, body=None, res=None):
		raise NotImplementedError('{} must be implemented onRequestSuccess'.format(self.__class__.__name__))

	def onRequestError(self, event: str, headers: dict = None, body=None, error=None):
		raise NotImplementedError('{} must be implemented onRequestError'.format(self.__class__.__name__))
