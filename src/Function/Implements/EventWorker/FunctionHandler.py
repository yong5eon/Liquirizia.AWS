# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function import FunctionHandler as Base
from Liquirizia.EventRunner import EventRunnerProperties
from Liquirizia.EventRunner.Errors import (
	NotSupportedEventError,
	NotSupportedBrokerError,
)

from .FunctionEventHandler import FunctionEventHandler
from .EventReader import EventReader

__all__ = (
	'FunctionHandler'
)


class FunctionHandler(Base):
	"""
	Event Runner Function Handler Class for Event Worker
	"""

	def __init__(
		self,
		handler: FunctionEventHandler,
		properties: EventRunnerProperties,
		reader: type(EventReader),
	):
		super(FunctionHandler, self).__init__(handler)
		self.handler = handler
		self.properties = properties
		self.reader = reader
		return

	def run(self, event):
		reader = self.reader(event)
		for queue, vhost, type, headers, body in reader:
			try:
				if self.handler:
					self.handler.onRequest(type, headers, body)
				if queue != self.properties.type.queue:
					raise NotSupportedBrokerError(queue)
				if type != self.properties.type.event:
					raise NotSupportedEventError(type)
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
