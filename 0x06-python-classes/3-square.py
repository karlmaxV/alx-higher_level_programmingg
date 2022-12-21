#!/usr/bin/python3

"""define a class sqaure."""

class Square:
"""represent a square"""
	def __init__(self, size=0):
	"""initialize a new square. 
	Args: Size(int): the size of the new square."""
	if not isinstance(size,int):
		raise TypeError("size msut be an integer")
	elif size < 0:
		raise ValueError("size must be >= 0")
	self.__size = size
	
	def area(self):
		"""return the current area of the square"""
		return(self.__size * self.__size)
