#!/usr/bin/python37


''' Defines a square class '''


class Square:
    """ This is a square class checks if the size is an integer or is < 0 """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
