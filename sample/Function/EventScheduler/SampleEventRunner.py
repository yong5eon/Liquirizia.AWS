# -*- coding: utf-8 -*-

from Liquirizia.EventRunner import EventRunner

__all__ = (
	'SampleEventRunner'
)


class SampleEventRunner(EventRunner):
	def __init__(self: str, event, headers: dict = None):
		self.event = event
		self.headers = headers
		return

	def run(self, body=None):
		print(self.event)
		print(self.headers)
		print(body)
		data = self.headers['a'] * body['c'] + self.headers['b']
		print(data)
		return data
