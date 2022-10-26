#!/usr/bin/python3
""Subclass of int"""


class MyInt(int):
	"""this class has its neq and eq operators inverted"""

	def __ne__(self, val):
		"""override parent __ne__ method"""
		return self.real == val

	def __eq__(self, val):
		"""override parent __eq__ method"""
		return self.real != val
