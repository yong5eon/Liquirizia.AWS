# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from .Errors import *

from .Implements.Text import Encoder as TextEncoder, Decoder as TextDecoder
from .Implements.JSON import Encoder as JSONEncoder, Decoder as JSONDecoder

__all__ = (
	'SerializerHelper'
)


class SerializerHelper(Singleton):
	"""
	Serializer Helper Class
	"""
	def onInit(self):
		self.serializers = {
			'text/plain': (TextEncoder, TextDecoder),
			'text': (TextEncoder, TextDecoder),
			'text/html': (TextEncoder, TextDecoder),
			'html': (TextEncoder, TextDecoder),
			'application/json': (JSONEncoder, JSONDecoder),
			'json': (JSONEncoder, JSONDecoder),
		}
		return

	@classmethod
	def Set(cls, format, encoder, decoder):
		helper = cls()
		helper.set(
			format,
			encoder=encoder,
			decoder=decoder
		)
		return

	def set(self, format, encoder, decoder):
		self.serializers[format.lower()] = (encoder(), decoder())
		return

	@classmethod
	def Get(cls, format):
		helper = cls()
		return helper.get(format)

	def get(self, format):
		if not format:
			return None, None

		encoder, decoder = self.serializers.get(format.lower(), (None, None))

		if not encoder or not decoder:
			raise NotSupportedError(format)

		return encoder(), decoder()

	@classmethod
	def GetEncoder(cls, format):
		helper = cls()
		return helper.encoder(format)

	def encoder(self, format):
		encoder, decoder = self.get(format)
		return encoder

	@classmethod
	def GetDecoder(cls, format):
		helper = cls()
		return helper.decoder(format)

	def decoder(self, format):
		encoder, decoder = self.get(format)
		return decoder

	@classmethod
	def Encode(cls, value, format=None, charset=None):
		helper = cls()
		return helper.encode(value, format, charset)

	def encode(self, value, format=None, charset=None):
		if not format:
			return str(value).encode(charset) if charset else str(value).encode()

		serializer = self.encoder(format)

		if not serializer:
			raise NotSupportedError(format)

		try:
			return serializer(value).encode(charset) if charset else serializer(value).encode()
		except BaseException as e:
			raise EncodeError(value, format, charset, e)

	@classmethod
	def Decode(cls, value, format=None, charset=None):
		helper = cls()
		return helper.decode(value, format, charset)

	def decode(self, value, format=None, charset=None):
		if not isinstance(value, (bytes, bytearray)):
			raise DecodeError(value, format, charset, RuntimeError('{} is not bytes'.format(value)))

		if not format:
			return value.decode(charset) if charset else value.decode()

		serializer = self.decoder(format)

		if not serializer:
			raise NotSupportedError(format)

		try:
			return serializer(value.decode(charset) if charset else value.decode())
		except BaseException as e:
			raise DecodeError(value, format, charset, e)
