# Liquirizia.AWS.Function.Implements.WebApplication
웹 어플리케이션을 AWS APIGateway를 위한 Lambda Function 으로 사용하기 위한 핸들러

## RequestRunner 를 AWS APIGateway 를 위한 Lambda Function 으로 만들기
웹 어플리케이션의 RequestRunnerImplements 를 사용하여 AWS의 Lambda Function Handler 를 만들어 준다.

### 웹 어플리케이션 정의
```python
from Liquirizia.WebApplication import RequestRunner, Request
from Liquirizia.WebApplication.Responses import *

__all__ = (
	'SampleRequestRunner'
)


class SampleRequestRunner(RequestRunner):
	def __init__(self, request: Request, parameters):
		self.request = request
		self.parameters = parameters
		return

	def run(self, body=None):
		return ResponseJSON({
			'parameters': self.parameters,
			'a': self.request.qs['a'] + body['a'],
			'b': self.request.qs['b'] + body['b'],
			'c': self.request.qs['c']
		})
```

### 웹 어플리케이션 속성 정의
```python
from Liquirizia.WebApplication import RequestRunnerProperties, RequestRunnerPropertiesHelper

from Liquirizia.WebApplication.Validator import Validator
from Liquirizia.WebApplication.Validator.Patterns import *

from SampleRequestRunner import SampleRequestRunner
from errors import *

properties = RequestRunnerProperties(
	SampleRequestRunner,
	method='POST',
	url='/sample/:id',
	qs=Validator(
		IsRequiredInDictionary('a', 'b', error=RequiredError('질의에 a 와 b 는 필수 입니다.')),
		IsDictionary({
			'a': Validator(
				TypeEvaluate(),
				IsInteger(
					IsGreaterThan(5, errorResponse=BadRequestErrorResponse('a 는 5보다 커야 합니다')),
					errorResponse=BadRequestErrorResponse('a 는 정수를 필요로 합니다.')
				)
			),
			'b': Validator(
				TypeEvaluate(),
				IsFloat(
					IsGreaterThan(9, errorResponse=BadRequestErrorResponse('b 는 9보다 커야 합니다')),
					errorResponse=BadRequestErrorResponse('b 는 실수(부동 소수점)을 필요로 합니다.')
				)
			),
			'c': Validator(
				SetDefault(''),
				IsString(errorResponse=BadRequestErrorResponse('c 는 문자열을 필요로 합니다.'))
			),
		}),
	),
	body=Validator(
		IsRequiredInDictionary('a', 'b', error=RequiredError('본문에 a 와 b 가 필요합니다.')),
		IsDictionary({
			'a': Validator(
				TypeEvaluate(),
				IsInteger(
					IsLessThan(5, errorResponse=BadRequestErrorResponse('a 는 5보다 작아야 합니다')),
					errorResponse=BadRequestErrorResponse('a 는 정수를 필요로 합니다.')
				)
			),
			'b': Validator(
				TypeEvaluate(),
				IsFloat(
					IsLessThan(9, errorResponse=BadRequestErrorResponse('b 는 9보다 작아야 합니다')),
					errorResponse=BadRequestErrorResponse('b 는 실수(부동 소수점)을 필요로 합니다.')
				)
			),
		}),
	)
)
```

### 함수 이벤트 핸들러 및 함수 핸들러 정의
```python
from Liquirizia.AWS.Function import FunctionHelper
from Liquirizia.AWS.Function.Implements.WebApplication import FunctionHandler
from Liquirizia.AWS.Function.Implements.WebApplication import FunctionEventHandler
from Liquirizia.WebApplication import RequestRunnerPropertiesHelper

from sys import stderr


# 함수 이벤트 핸들러 정의
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

	def onRequest(self, request):
		print('REQUEST         : {}'.format(request))
		return

	def onRequestSuccess(self, request, response):
		print('REQUEST SUCCESS : {} - {}\n{}'.format(request, response, response.body.decode('utf-8')))
		return

	def onRequestError(self, request, error):
		print('REQUEST ERROR   : {} - {}'.format(request, str(error)), file=stderr)
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


# 함수 핸들러 설정
Handler = FunctionHelper.Get(
	FunctionHandler,
	SampleFunctionEventHandler(),
	RequestRunnerPropertiesHelper.Load('SampleWebApplication.conf')
)
```

## RequestFilter 를 AWS CloudFront 를 위한 Lambda@Edge Function 으로 만들기

### 요청을 변환 하는 방법
```python
from Liquirizia.AWS.Function import FunctionHelper
from Liquirizia.AWS.Function.Implements.WebApplication.RequestFilter import FunctionHandler, FunctionEventHandler

from Liquirizia.WebApplication import RequestFilter, Request, Response


# 이벤트 핸들러 정의
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

	def onRequestFilter(self, request):
		print('FILTER          : {}'.format(request))
		return

	def onRequestFilterSuccess(self, request: Request, response: Response):
		print('FILTER  SUCCESS : {}'.format(request))
		if response:
			print('\n{}\n{}'.format(response, response.body.decode('utf-8')))
		return

	def onRequestFilterError(self, request, error: Error):
		print('FILTER  ERROR   : {} - {}'.format(request, str(error)), file=stderr)
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


# 요청 필터 정의
class SampleRequestFilter(RequestFilter):
	def run(self, request: Request) -> tuple[Request, (Response, None)]:
		request.header('X-Addition-Header', 'SampleRequestFilter')
		return request, None
	
	
# 람다 함수 핸들러 정의
Handler = FunctionHelper.Get(
	FunctionHandler,
	SampleFunctionEventHandler(),
	SampleRequestFilter()
)
```

### 응답을 반환하는 방법
```python
from Liquirizia.AWS.Function import FunctionHelper
from Liquirizia.AWS.Function.Implements.WebApplication.RequestFilter import FunctionHandler, FunctionEventHandler

from Liquirizia.WebApplication import RequestFilter, Request, Response, Error
from Liquirizia.WebApplication.Responses import ResponseRedirect

from sys import stderr


# 이벤트 핸들러 정의
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

	def onRequestFilter(self, request):
		print('FILTER          : {}'.format(request))
		return

	def onRequestFilterSuccess(self, request: Request, response: Response):
		print('FILTER  SUCCESS : {}'.format(request))
		if response:
			print('\n{}\n{}'.format(response, response.body.decode('utf-8')))
		return

	def onRequestFilterError(self, request, error: Error):
		print('FILTER  ERROR   : {} - {}'.format(request, str(error)), file=stderr)
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


# 요청 필터 정의
class SampleRequestFilter(RequestFilter):
	def run(self, request: Request) -> tuple[Request, (Response, None)]:
		return request, ResponseRedirect('/')
	
	
# 람다 함수 핸들러 정의
Handler = FunctionHelper.Get(
	FunctionHandler,
	SampleFunctionEventHandler(),
	SampleRequestFilter()
)
```

## ResponseFilter 를 AWS CloudFront 를 위한 Lambda@Edge Function 으로 만들기
```python
from Liquirizia.AWS.Function import FunctionHelper
from Liquirizia.AWS.Function.Implements.WebApplication.ResponseFilter import FunctionHandler, FunctionEventHandler

from Liquirizia.WebApplication import ResponseFilter, Response, Error
from Liquirizia.WebApplication.Responses import ResponseOK

from sys import stderr


# 이벤트 핸들러 정의
class SampleFunctionEventHandler(FunctionEventHandler):
	def onInitialize(self):
		print('INITIALIZE')
		return

	def onEventResponse(self, name, version, arn, limit, timeout, tag=None):
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

	def onResponseFilter(self, response):
		print('FILTER          : {}'.format(response))
		return

	def onResponseFilterSuccess(self, response: Response):
		print('FILTER  SUCCESS : {}'.format(response))
		return

	def onResponseFilterError(self, response, error: Error):
		print('FILTER  ERROR   : {} - {}'.format(response, str(error)), file=stderr)
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


# 요청 필터 정의
class SampleResponseFilter(ResponseFilter):
	def run(self, response: Response) -> Response:
		return ResponseOK('New World', format='text/plain', charset='utf-8')
	
	
# 람다 함수 핸들러 정의
Handler = FunctionHelper.Get(
	FunctionHandler,
	SampleFunctionEventHandler(),
	SampleResponseFilter()
)
```