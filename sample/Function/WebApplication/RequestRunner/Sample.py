# -*- coding: utf-8 -*-

from Liquirizia.AWS.Function import FunctionHelper
from Liquirizia.AWS.Function.Implements.WebApplication import FunctionHandler

from Liquirizia.WebApplication import RequestRunnerPropertiesHelper
from SampleFunctionEventHandler import SampleFunctionEventHandler

from json import loads


if __name__ == '__main__':

	Handler = FunctionHelper.Get(
		FunctionHandler,
		SampleFunctionEventHandler(),
		RequestRunnerPropertiesHelper.Load('SampleRequestRunner.conf')
	)

	with open('.event.success', encoding='utf-8') as f:
		event = loads(f.read())
		response = Handler(event, None)
		print(response)
	with open('.event.error', encoding='utf-8') as f:
		event = loads(f.read())
		response = Handler(event, None)
		print(response)
