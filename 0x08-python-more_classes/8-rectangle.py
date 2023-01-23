#!/usr/bin/python3
"""
Class Rectangle: Defines a rectangle based on 7-rectangle.py
"""


class Rectangle:
    """class that defines a rectangle with his attributes"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize attributes"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if (rect_1.area() >= rect_2.area()):
                return rect_1
            return rect_2

    @property
    def width(self):
        """get the value of the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            width (int): the width of the square.
        Raises:
            TypeError: if width is not given as an integer.
            ValueError: if width is less than 0.
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the value of the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            height (int): the height of the square.
        Raises:
            TypeError: if width is not given as an integer.
            ValueError: if height is less than 0.
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Retrieves the area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Retrieves the perimeter of the Rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """magic method that prints the rectangle with the character #"""
        string = ""
        if (self.__width == 0 or self.__height == 0):
            return (string)
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += str(self.print_symbol)
                string += "\n"
            string = string[:-1]
            return (string)

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        wid = str(self.__width)
        hei = str(self.__height)
        return "Rectangle(" + wid + ", " + hei + ")"

    def __del__(self):
        """(destruct) Detect when an instance of Rectangle
        is deleted and print a message
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
