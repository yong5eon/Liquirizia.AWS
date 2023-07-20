# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from .FunctionHandler import FunctionHandler
from .FunctionEventHandler import FunctionEventHandler

__all__ = (
	'FunctionHelper'
)


class FunctionHelper(Singleton):

	def onInit(self):
		return

	@classmethod
	def Get(cls, fn: type(FunctionHandler), event: FunctionEventHandler, *args, **kwargs):
		helper = cls()
		return helper.get(fn, event, *args, **kwargs)

	def get(self, fn: type(FunctionHandler), event: FunctionEventHandler, *args, **kwargs):
		return fn(event, *args, **kwargs)
