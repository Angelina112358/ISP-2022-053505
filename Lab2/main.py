import math
from serialize.serializer import *
from parsers.json import *
from factory.factory import Factory

c = 42


def f(x):
    a = 123
    return math.sin(a*x*c)


class Person:
    def __init__(self):
        self.name = 'Vlad'
        self.age = 19
        self.temp_list = [1, 2, 3]
        self.temp_dict = {'a': 20, 'b': 30}


def main():

    factory = Factory.create_serializer('json')
    pers = Person().__dict__
    ser = factory.dumps(pers)
    print(ser)


if __name__ == '__main__':
    main()
