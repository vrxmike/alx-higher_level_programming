#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
	"""A square representation"""
	def __init__(self, size):
		"""An instantiation of square"""
		self.integeer_validator("size", size)
		self.__size = size
		super().__init__(size, size)

	def area(self):
		"""Gets the area of the square"""
		return self.__size * self.__size
