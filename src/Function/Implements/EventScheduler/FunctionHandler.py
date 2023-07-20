# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function import FunctionHandler as Base
from Liquirizia.EventRunner import EventRunnerProperties
from Liquirizia.EventRunner.Errors import (
	NotSupportedEventError,
	NotSupportedBrokerError,
)

from .FunctionEventHandler import FunctionEventHandler

__all__ = (
	'FunctionHandler'
)


class FunctionHandler(Base):
	"""
	Event Runner Function Handler Class for Event Scheduler
	"""

	def __init__(
		self,
		handler: FunctionEventHandler,
		properties: EventRunnerProperties,
	):
		super(FunctionHandler, self).__init__(handler)
		self.handler = handler
		self.properties = properties
		return

	def run(self, event):
		type = self.properties.type.event
		headers = self.properties.type.headers
		body = self.properties.type.body
		try:
			if self.handler:
				self.handler.onRequest(type, headers, body)
			if self.properties.header:
				headers = self.properties.header(headers)
			if self.properties.body:
				body = self.properties.body(body)
			obj = self.properties.object(type, headers)
			res = obj.run(body)
			for callback in self.properties.completes if self.properties.completes else []:
				callback(type, headers, body, res)
			if self.handler:
				self.handler.onRequestSuccess(type, headers, body, res)
		except BaseException as e:
			for callback in self.properties.errors if self.properties.errors else []:
				callback(type, headers, body, e)
			if self.handler:
				self.handler.onRequestError(type, headers, body, e)
		return
