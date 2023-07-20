# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function.Errors import *

from ...EventReader import EventReader as EventReaderBase
from ...Serializer import SerializerHelper

from base64 import b64decode

__all__ = (
	'EventReader'
)


class EventReader(EventReaderBase):
	"""
	Event Reader for RabbitMQ
	"""
	def __init__(self, event):
		self.__events__ = []
		if 'rmqMessagesByQueue' not in event:
			raise InvalidEventError()
		for queue, messages in event['rmqMessagesByQueue'].items():
			q, vhost = queue.split('::/')
			for message in messages:
				type = self.__parse__(message['basicProperties']['type'])
				format = self.__parse__(message['basicProperties']['contentType'])
				charset = self.__parse__(message['basicProperties']['contentEncoding'])
				headers = self.__parse__(message['basicProperties']['headers'])
				body = SerializerHelper.Decode(b64decode(message['data']), format, charset) if self.__parse__(message['data']) else None
				self.__events__.append((q, vhost, type, headers, body))
		return

	def __getitem__(self, index):
		return self.__events__[index]

	def __len__(self):
		return len(self.__events__)

	def __iter__(self):
		return self.__events__.__iter__()

	def __parse__(self, v):
		if isinstance(v, str) and v == 'None':
			return None
		return v
