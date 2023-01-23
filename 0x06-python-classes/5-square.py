#!/usr/bin/python3
"""
Square class: defines a square
"""


class Square:
    """class Square that defines a squaare"""
    def __init__(self, size=0):
        """Initialize attributes"""
        self.size = size

    @property
    def size(self):
        """Return the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the size of one edge of the square.
        Raises:
            TypeError: if size is not given as an integer.
            ValueError: if size is less than 0.
        """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
