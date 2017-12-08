# https://python.swaroopch.com/exceptions.html

class ShortInputException(Exception):
    '''A user-defined exception class'''
    def __init__(self, length, atleast)
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
