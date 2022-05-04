import math
from factory.factory import Factory
from serialize.serializer import *

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
        self.exp = 45


def main():
    pers = Person().__dict__
    
    factory = Factory.create_serializer('json')
    s = factory.dumps(f)
    a = factory.loads(s)
    print(a(5))

    factory = Factory.create_serializer('yml')
    s = factory.dumps(f)
    a = factory.loads(s)
    print(a(5))

    factory = Factory.create_serializer('toml')
    s = factory.dumps(f)
    a = factory.loads(s)
    print(a(5))


if __name__ == '__main__':
    main()
