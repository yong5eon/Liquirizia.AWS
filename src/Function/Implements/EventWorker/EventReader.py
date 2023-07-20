# -*- coding: utf-8 -*-

__all__ = (
	'EventReader'
)


class EventReader(object):
	"""
	Event Reader Interface

	- iterable
	"""
	def __getitem__(self, index):
		raise NotImplementedError('{} must be implemented __getitem__'.format(self.__class__.__name__))

	def __len__(self):
		raise NotImplementedError('{} must be implemented __len__'.format(self.__class__.__name__))

	def __iter__(self):
		raise NotImplementedError('{} must be implemented __iter__'.format(self.__class__.__name__))
