#!/usr/bin/python37

''' Defines a square class '''

class Square:

    """ This is a square class checks if the size is an integer or is less than zero """

    def __init__(self, size=0):
        self.size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

