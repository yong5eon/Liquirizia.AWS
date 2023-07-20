# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function.Errors import *

from ....EventReader import EventReader as EventReaderBase
from ....Serializer import SerializerHelper

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
		if 'Records' not in event:
			raise InvalidEventError()
		for record in event['Records']:
			arn = record['eventSourceARN'].split(':')
			queue = arn[len(arn)-1]
			type = record['messageAttributes']['Type']['stringValue']
			format = record['messageAttributes']['ContentType']['stringValue']
			charset = record['messageAttributes']['ContentEncoding']['stringValue']
			headers = SerializerHelper.Decode(
				b64decode(record['messageAttributes']['Headers']['binaryValue']),
				'application/json',
				'utf-8'
			) if 'Headers' in record['messageAttributes'] else None
			body = SerializerHelper.Decode(record['body'].encode(charset), format, charset)
			self.__events__.append((queue, None, type, headers, body))
		return

	def __getitem__(self, index):
		return self.__events__[index]

	def __len__(self):
		return len(self.__events__)

	def __iter__(self):
		return self.__events__.__iter__()
