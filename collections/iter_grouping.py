import functools
from itertools import *
import operator
import pprint

@functools.total_ordering
class Section:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.a}, {self.b}'

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)

    def __gt__(self, other):
        return (self.a, self.b) > (other.a, other.b)