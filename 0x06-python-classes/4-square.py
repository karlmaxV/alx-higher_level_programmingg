#!/usr/bin/python3

"""define a class square"""

class Square:
"""represent a square"""
	def __init__(self,size=0):
		"""initialize a new square
		Args:
			size (int): the size of the neq square.
		"""
		self.__size = size

		@property
		def size(self):
			"""get/set the current size of the square"""
			return (self.__size)
		@size.setter
		def size(selft, value):
			if not isinstance(value, int):
				raise TypeError("size must be an interger")
			elif value < 0:
				raise ValueError("size must be >=0")
			self.__size = size

		def area(self):
			"""return the current area of the sqaure"""
			return (self.__size * self.__size)
