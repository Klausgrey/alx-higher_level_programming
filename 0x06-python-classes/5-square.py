#!/usr/bin/python37


''' Defines a square class '''


class Square:
    """ This is a square class checks if the size is an integer or is < 0 """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ Public instance method that returns size """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range (0, self.__size):
            for j in range (0, self.__size):
                print("#", end="")
            print()