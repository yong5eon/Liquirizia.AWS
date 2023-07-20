# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import (
	RequestFilter,
	Request,
	Response,
)

__all__ = (
	'SampleRequestFilterAddHeader'
)


class SampleRequestFilterAddHeader(RequestFilter):
	def run(self, request: Request) -> tuple[Request, (Response, None)]:
		request.header('X-Addition-Header', 'SampleRequestFilter')
		return request, None
