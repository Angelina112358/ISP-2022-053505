from serialize.serializer import *
from factory.factory import Factory
import json


def main():
    parser = Factory.create_serializer('json')
    #a = {'a': True}
    #print(serialize(a))
    #print(parser.dumps(a))
    #s = json.dumps(a)
    #print(parser.loads(s))



if __name__ == '__main__':
    main()
