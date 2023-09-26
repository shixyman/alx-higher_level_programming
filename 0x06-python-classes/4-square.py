#!/usr/bin/python3
"""define a class Square in python"""


class Square:
    """Square class """
    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.size = size  #: size of the square
    def area(self):
        """calculates the square's area
            Returns:
            The area of the square
        """
        return (self.__size) ** 2
    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size
    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
            value (int): size of the square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square
