#!/usr/bin/python3

"""Define a class square."""

class Square:
	"""represent a new square."""

	def __init__(self,size=0):
		"""initialize a new square.
		Args:
			Size (int): The size of the new sqaure."""

		if not isinstance(size,int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise valueError("size must be >= 0")
		self.__size = size
