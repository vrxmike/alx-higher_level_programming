#!/usr/bin/python3
"""
Class that inherits from BaseGeometry
"""

BaseGeometry =  __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
	"""A subclass of BaseGeometry"""
	def __init__(self, width, height):
		"""An instantiation of the rectangle"""
	self.integer_validator("width", width)
	self.__width = width
	self.integer_validator("height", height)
	self.__height = height

	def area(self):
		"""returns the area"""
		return self.__width * self.__height

	def __str__(self):
		"""Formats to string"""
	return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
