#!/usr/bin/python3

"""define a class Square"""
class Square:
    """represent a sqaure"""
    def __init__(self, size =0, position=(0,0)):
        """initialize a new sqaure
        Args:
            size (int): The size of the new sqaure.
            position (int, int): the position of th new square.
        """
        self.size = size
        self.position = position

        @property
        def size(self):
            """get/set the current size of the square"""
            return (self.__size)

        @size.setter
        def size(self,value):
            if not isinstance(value,int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError ("size must be >= 0")
            self.__size = value

        @property
        def position(self):
            """get/set the current position of the square"""
            return (self.__position)
        
        @position.setter
        def position(self,value):
            if (not isinstance(value,tuple) or
                    len(value)!= 2 or
                    not all (isinstance(num, int)for num in value) or
                    not all (num >= 0 for num in value)):
                raise TypeError("positon must be a tuple of 2 position integers")
                self.__position = value
        def area(self):
            """return the current area of the sqaure"""
            return (self.__size * self.__size)
        def my_print(self):
            """print the square with the # character"""
            if self.__size == 0:
                print("")
                return
            [print("")for i in range(0,self.__position[1])]
            for i in range(0,self.__size):
                [print(" ", end="")for j in range(0,self.__position[0])]
                [print("#", end="")for k in range(0,self.__size)]
                print("")
