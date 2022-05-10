import math

c = 42


def f(x):
    a = 123
    return math.sin(x*a*c)


def add(x, y):
    return x + y


class Obj:
    def __init__(self):
        self.sstr = 'string'
        self.number = 100
        self.llist = [1, 2, 'elem']
        self.ddict = {'key': 'value'}
        self.ttuple = ('el1', 'el2', 'el3')