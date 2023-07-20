# -*- coding: utf-8 -*-

from Liquirizia.WebApplication.Validator import ErrorResponse
from Liquirizia.WebApplication.Responses import (
	ResponseBadRequest,
)

__all__ = (
	'BadRequestErrorResponse'
)


class BadRequestErrorResponse(ErrorResponse):
	def __init__(self, format):
		self.format = format
		return

	def __call__(self, parameter, *args, **kwargs):
		return ResponseBadRequest(self.format, 'text/plain', 'utf-8')
