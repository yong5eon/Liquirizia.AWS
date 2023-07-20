# -*- coding: utf-8 -*-

from Liquirizia.EventRunner import EventRunnerPropertiesHelper
from Liquirizia.AWS.Function import FunctionHelper
from Liquirizia.AWS.Function.Implements.EventScheduler import FunctionHandler

from SampleFunctionEventHandler import SampleFunctionEventHandler

import json

if __name__ == '__main__':

	Handler = FunctionHelper.Get(
		FunctionHandler,
		SampleFunctionEventHandler(),
		EventRunnerPropertiesHelper.Load('SampleEventRunner.Interval.conf'),
	)

	with open('.event') as f:
		event = json.loads(f.read())
		Handler(event, None)

	Handler = FunctionHelper.Get(
		FunctionHandler,
		SampleFunctionEventHandler(),
		EventRunnerPropertiesHelper.Load('SampleEventRunner.Timer.conf'),
	)

	with open('.event') as f:
		event = json.loads(f.read())
		Handler(event, None)
