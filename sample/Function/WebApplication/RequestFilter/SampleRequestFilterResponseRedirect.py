# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import (
	RequestFilter,
	Request,
	Response,
)
from Liquirizia.WebApplication.Responses import ResponseRedirect

__all__ = (
	'SampleRequestFilterResponseRedirect'
)


class SampleRequestFilterResponseRedirect(RequestFilter):
	def run(self, request: Request) -> tuple[Request, (Response, None)]:
		return request, ResponseRedirect('/')
