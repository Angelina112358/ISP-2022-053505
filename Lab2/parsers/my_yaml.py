from serialize.serializer import *
import inspect
import yaml
import os


def dump(obj, fp):
    if inspect.isroutine(obj):
        obj = serialize(obj)
    with open(fp, 'w') as f:
        yaml.dump(obj, f)
    return fp


def dumps(obj):
    if inspect.isroutine(obj):
        obj = serialize(obj)
    fp = dump(obj, 'temp.yml')
    with open(fp, 'r') as f:
        t = f.read()
    os.remove('temp.yml')
    return t


def load(fp):
    with open(fp, 'r') as f:
        t = yaml.load(f, Loader=yaml.FullLoader)
    return deserialize(t)


def loads(s):
    with open('temp.yml', 'w') as f:
        f.write(s)
    t = load('temp.yml')
    os.remove('temp.yml')
    return t