# -*- coding: utf-8 -*-

from Liquirizia.EventRunner import EventRunnerPropertiesHelper
from Liquirizia.AWS.Function import FunctionHelper
from Liquirizia.AWS.Function.Implements.EventWorker import FunctionHandler
from Liquirizia.AWS.Function.Implements.EventWorker.Types.RabbitMQ import EventReader as RMQEventReader
from Liquirizia.AWS.Function.Implements.EventWorker.Types.AWS.SimpleNotificationQueueService import EventReader as SQSEventReader

from SampleFunctionEventHandler import SampleFunctionEventHandler

import json

if __name__ == '__main__':

	Handler = FunctionHelper.Get(
		FunctionHandler,
		SampleFunctionEventHandler(),
		EventRunnerPropertiesHelper.Load('SampleEventRunner.RabbitMQ.conf'),
		RMQEventReader
	)

	with open('.event.RabbitMQ') as f:
		event = json.loads(f.read())
		Handler(event, None)

	Handler = FunctionHelper.Get(
		FunctionHandler,
		SampleFunctionEventHandler(),
		EventRunnerPropertiesHelper.Load('SampleEventRunner.AWS.SimpleNotificationQueueService.conf'),
		SQSEventReader
	)

	with open('.event.AWS.SimpleNotificationQueueService') as f:
		event = json.loads(f.read())
		Handler(event, None)
