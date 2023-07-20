# Liquirizia.AWS.Function.Implements.EventWorker
이벤트 어플리케이션(EventRunner)을 이벤트 워커(EventWorker)형식의 아마존 웹 서비스 람다 함수로 사용하기 위한 핸들러

## 사용방법

### 이번트 어플리케이션 정의
```python
from Liquirizia.EventRunner import EventRunner

class SampleEventRunner(EventRunner):
	def __init__(self: str, event, headers: dict = None):
		self.event = event
		self.a = headers['a']
		self.b = headers['b']
		return

	def run(self, body=None):
		return self.a * body + self.b
```

### 이벤트 어플리케이션의 속성
```python
from Liquirizia.EventRunner import EventRunnerProperties
from Liquirizia.EventRunner.Types import EventWorker
from Liquirizia.EventRunner.Errors import InvalidHeaderError, InvalidBodyError

from Liquirizia.Validator import Validator, Error, Pattern
from Liquirizia.Validator.Patterns import *

from SampleEventRunner import SampleEventRunner

class IsCompare(Pattern):
	def __init__(self, error: Error = None):
		self.error = error
		return

	def __call__(self, parameter):
		if not parameter['a'] > parameter['b']:
			if self.error:
				raise self.error(parameter)
			raise RuntimeError('a must be greater than b')
		return parameter


properties = EventRunnerProperties(
	SampleEventRunner,
	type=EventWorker('event.sample.compute', 'Sample', 'queue.sample'),
	header=Validator(
		IsRequiredInDictionary('a', 'b'),
		IsDictionary({
			'a': Validator(IsInteger()),
			'b': Validator(IsInteger()),
		}),
		IsCompare()
	),
	body=Validator(IsInteger(IsGreaterThan(0)))
)
```

### 함수 이벤트 핸들러 정의
```python
from Liquirizia.AWS.Function.Implements.EventWorker import FunctionEventHandler

from sys import stderr

__all__ = (
	'SampleFunctionEventHandler'
)


class SampleFunctionEventHandler(FunctionEventHandler):
	def onInitialize(self):
		print('INITIALIZE')
		return

	def onEventRequest(self, name, version, arn, limit, timeout, tag=None):
		print('EVENT REQUEST   : {}, {}, {}, {}, {}, {}'.format(
			name,
			version,
			arn,
			limit,
			timeout,
			tag
		))

	def onEvent(self, event):
		print('EVENT           : {}'.format(event))
		return

	def onRequest(self, event: str, headers: dict = None, body=None):
		print('REQUEST         : {}, {}, {}'.format(event, headers, body))
		return

	def onRequestSuccess(self, event: str, headers: dict = None, body=None, res=None):
		print('REQUEST SUCCESS : {}'.format(res))
		return

	def onRequestError(self, event: str, headers: dict = None, body=None, error=None):
		print('REQUEST ERROR   : {}'.format(str(error)), file=stderr)
		return

	def onEventSuccess(self, event, res=None):
		print('EVENT SUCCESS   : {} - {}'.format(event, str(res) if res else ''))
		return

	def onEventError(self, event, error=None):
		print('EVENT ERROR     : \n{}\n{}'.format(event, str(error) if error else ''), file=stderr)
		return

	def onRelease(self):
		print('RELEASE')
		return
```

### 함수 핸들러 정의
```python
from Liquirizia.AWS.Function import FunctionHelper
from Liquirizia.AWS.Function.Implements.EventWorker import FunctionHandler
from Liquirizia.AWS.Function.Implements.EventWorker.Types.RabbitMQ import EventReader

from Liquirizia.EventRunner import EventRunnerPropertiesHelper

from SampleFunctionEventHandler import SampleFunctionEventHandler

Handler = FunctionHelper.Get(
	FunctionHandler,
	SampleFunctionEventHandler(),
	EventRunnerPropertiesHelper.Load('${PROPERTIES_PATH}'),
	EventReader
)
```