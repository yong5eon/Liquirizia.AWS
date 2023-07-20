# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function import FunctionHelper
from Liquirizia.AWS.Function.Implements.WebApplication.RequestFilter import FunctionHandler

from SampleFunctionEventHandler import SampleFunctionEventHandler

from SampleRequestFilterAddHeader import SampleRequestFilterAddHeader
from SampleRequestFilterResponseRedirect import SampleRequestFilterResponseRedirect

from json import loads

if __name__ == '__main__':

	Handler = FunctionHelper.Get(
		FunctionHandler,
		SampleFunctionEventHandler(),
		SampleRequestFilterAddHeader()
	)

	with open('.event', encoding='utf-8') as f:
		event = loads(f.read())
		response = Handler(event, None)
		print(response)

	Handler = FunctionHelper.Get(
		FunctionHandler,
		SampleFunctionEventHandler(),
		SampleRequestFilterResponseRedirect()
	)

	with open('.event', encoding='utf-8') as f:
		event = loads(f.read())
		response = Handler(event, None)
		print(response)
