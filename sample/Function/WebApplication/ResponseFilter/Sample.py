# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function import FunctionHelper
from Liquirizia.AWS.Function.Implements.WebApplication.ResponseFilter import FunctionHandler

from SampleFunctionEventHandler import SampleFunctionEventHandler

from SampleResponseFilter import SampleResponseFilter

from json import loads

if __name__ == '__main__':

	Handler = FunctionHelper.Get(
		FunctionHandler,
		SampleFunctionEventHandler(),
		SampleResponseFilter()
	)

	with open('.event', encoding='utf-8') as f:
		event = loads(f.read())
		response = Handler(event, None)
		print(response)
