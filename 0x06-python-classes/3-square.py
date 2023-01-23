#!/usr/bin/python3
"""Square Class: Defines a square"""


class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the size of one edge of the square.
        Raises:
            TypeError: if size is not given as an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Gives the area of the square"""
        return (self.__size * self.__size)
