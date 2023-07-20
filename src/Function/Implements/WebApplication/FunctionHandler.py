# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function import FunctionHandler as Base

from Liquirizia.WebApplication import (
	RequestRunnerProperties,
	Error
)
from Liquirizia.WebApplication.Errors import InternalServerError

from .FunctionEventHandler import FunctionEventHandler
from .RequestReader import RequestReader
from .ResponseWriter import ResponseWriter

from re import compile, escape

__all__ = (
	'FunctionHandler'
)


class FunctionHandler(Base):
	"""
	Web Application Function Handler Class
	"""

	RegexVar = compile(r':\w+')

	def __init__(
		self,
		handler: FunctionEventHandler,
		properties: RequestRunnerProperties,
	):
		super(FunctionHandler, self).__init__(handler)
		self.handler = handler
		self.object = properties['object']
		self.method = properties['method']
		self.url = properties['url']
		self.onRequest = properties['onRequest']
		self.onRequestOrigin = properties['onRequestOrigin']
		self.onResponseOrigin = properties['onResponseOrigin']
		self.onResponse = properties['onResponse']
		self.qs = properties['qs']
		self.body = properties['body']
		self.parameter = ':%s'
		self.re, self.fmt = self.parse(self.url)
		return

	def run(self, event):

		request = None

		try:
			request = RequestReader(event)

			m, parameters = self.match(request.path)

			if not m:
				raise InternalServerError(reason='{} is invalid uri'.format(request.uri))

			if request.method != self.method:
				raise InternalServerError(reason='{} is invalid method'.format(request.method))

			self.handler.onRequest(request)

			if self.onRequest:
				request, response = self.onRequest.run(request)
				if response:
					self.handler.onRequestSuccess(request, response)
					return ResponseWriter(response)

			if self.onRequestOrigin:
				request, response = self.onRequestOrigin.run(request)
				if response:
					self.handler.onRequestSuccess(request, response)
					return ResponseWriter(response)

			if self.qs:
				request.qs, response = self.qs(request.qs)
				if response:
					self.handler.onRequestSuccess(request, response)
					return ResponseWriter(response)

			if self.body:
				request.body, response = self.body(request.body)
				if response:
					self.handler.onRequestSuccess(request, response)
					return ResponseWriter(response)

			obj = self.object(request, parameters)
			response = obj.run(request.body)

			if self.onResponseOrigin:
				response = self.onResponseOrigin.run(response)

			if self.onResponse:
				response = self.onResponse.run(response)

			self.handler.onRequestSuccess(request, response)
			return ResponseWriter(response)
		except Error as e:
			self.handler.onRequestError(request, error=e)
			raise e

	def match(self, url: str):
		m = self.re.match(url)
		if not m:
			return False, None
		return True, m.groupdict()

	def parse(self, url: str):
		fmt = []
		regex = []
		pos = 0

		for match in FunctionHandler.RegexVar.finditer(url):
			regex.append(escape(url[pos:match.start()]))
			fmt.append(url[pos:match.start()])

			regex.append('(?P<%s>%s)' % (match.group()[1:], '[^/]+'))
			fmt.append(self.parameter % (match.group()[1:],))

			pos = match.end()

		regex.append(escape(url[pos:]))
		fmt.append(url[pos:])

		return compile('^%s$' % "".join(regex)), "".join(fmt)
