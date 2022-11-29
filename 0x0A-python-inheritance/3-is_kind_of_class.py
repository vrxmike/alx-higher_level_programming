#!/usr/bin/python3
"""Function"""


def is_kind_of_class(obj, a_class):
	"""Check if obj is an instance of a class that inherited from a_class"""
	return (isinstance(obj, a_class))
