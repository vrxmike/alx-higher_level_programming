#!/usr/bin/python3
"""Check whether object is an instance"""


def inherit_from(obj, a_class):
	"""Is obj a subclass of a_class"""
	return (issubclass(type(obj), a_class) and type(obj) != a_class)
