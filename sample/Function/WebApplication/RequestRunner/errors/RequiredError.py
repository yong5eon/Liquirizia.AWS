# -*- coding: utf-8 -*-

from Liquirizia.WebApplication.Validator import Error
from Liquirizia.WebApplication.Errors import (
	BadRequestError
)

__all__ = (
	'RequiredError'
)


class RequiredError(Error):
	def __init__(self, format):
		self.format = format
		return

	def __call__(self, parameter, *args, **kwargs):
		return BadRequestError(reason=self.format)
