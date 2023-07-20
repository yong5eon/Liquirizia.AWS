# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import (
	ResponseFilter,
	Response,
)
from Liquirizia.WebApplication.Responses import ResponseOK

__all__ = (
	'SampleResponseFilter'
)


class SampleResponseFilter(ResponseFilter):
	def run(self, response: Response) -> Response:
		return ResponseOK('New World', format='text/plain', charset='utf-8')
