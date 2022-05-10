import os
from unittest import TestCase, main
from tests.test_objects import *
from factory.factory import Factory
from serialize.serializer import *
import json
import yaml
import qtoml


class Test(TestCase):

    def tests_json_dumps(self):
        obj = Obj().__dict__
        parser = Factory.create_serializer('json')
        self.assertEqual(parser.dumps(obj), json.dumps(obj))

    def tests_yaml_dump(self):
        obj = Obj().__dict__
        parser = Factory.create_serializer('yml')
        parser.dump(obj, 'test1.yml')
        with open('test2.yml', 'w') as file:
            yaml.dump(obj, file)

        with open('test1.yml', 'r') as file:
            s1 = file.read()
        with open('test2.yml', 'r') as file:
            s2 = file.read()
        os.remove('test1.yml')
        os.remove('test2.yml')
        self.assertEqual(s1, s2)

    def tests_toml_dumps(self):
        obj = Obj().__dict__
        parser = Factory.create_serializer('toml')
        self.assertEqual(parser.dumps(obj), qtoml.dumps(obj))

    def tests_json_dump(self):
        parser = Factory.create_serializer('json')
        obj = Obj().__dict__
        parser.dump(obj, 'test1.json')
        with open('test1.json', 'r') as file:
            s1 = file.read()
        with open('test2.json', 'w') as file:
            json.dump(obj, file)
        with open('test2.json', 'r') as file:
            s2 = file.read()
        os.remove('test1.json')
        os.remove('test2.json')
        self.assertEqual(s1, s2)

    def tests_toml_dump(self):
        parser = Factory.create_serializer('toml')
        obj = Obj().__dict__
        parser.dump(obj, 'test1.toml')
        with open('test1.toml', 'r') as file:
            s1 = file.read()
        with open('test2.toml', 'w') as file:
            qtoml.dump(obj, file)
        with open('test2.toml', 'r') as file:
            s2 = file.read()
        os.remove('test1.toml')
        os.remove('test2.toml')
        self.assertEqual(s1, s2)

    def tests_json_load(self):
        parser = Factory.create_serializer('json')
        obj = Obj().__dict__
        sr = parser.dump(obj, 'test1.json')
        obj1 = parser.load('test1.json')
        with open('test2.json', 'w') as file:
            json.dump(obj, file)
        with open('test2.json', 'r') as file:
            obj2 = json.load(file)
        os.remove('test1.json')
        os.remove('test2.json')
        self.assertEqual(obj1, obj2)

    def tests_json_loads(self):
        parser = Factory.create_serializer('json')
        obj = Obj().__dict__
        sr = parser.dumps(obj)
        s1 = parser.loads(sr)
        s2 = json.loads(sr)
        self.assertEqual(s1, s2)

    def tests_yaml_load(self):
        parser = Factory.create_serializer('yml')
        obj = Obj().__dict__
        sr = parser.dump(obj, 'test1.yaml')
        obj1 = parser.load('test1.yaml')
        with open('test2.yaml', 'w') as file:
            yaml.dump(obj, file)
        with open('test2.yaml') as file:
            obj2 = yaml.load(file, Loader=yaml.FullLoader)
        os.remove('test1.yaml')
        os.remove('test2.yaml')
        self.assertEqual(obj1, obj2)

    def tests_toml_load(self):
        parser = Factory.create_serializer('toml')
        obj = Obj().__dict__
        sr = parser.dump(obj, 'test1.toml')
        obj1 = parser.load('test1.toml')
        with open('test2.toml', 'w') as file:
            qtoml.dump(obj, file)
        with open('test2.toml', 'r') as file:
            obj2 = qtoml.load(file)
        os.remove('test1.toml')
        os.remove('test2.toml')
        self.assertEqual(obj1, obj2)

    def test_func(self):
        s = serialize(f)
        foo = deserialize(s)
        self.assertEqual(foo(5), f(5))


if __name__ == '__main__':
    main()