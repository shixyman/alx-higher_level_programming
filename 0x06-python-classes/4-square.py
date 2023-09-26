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
        return (self.__size) ** 2i
     @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
