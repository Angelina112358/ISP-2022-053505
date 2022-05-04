from serialize.serializer import *
import inspect
import qtoml


def dump(obj, fp):
    with open(fp, 'w') as f:
        f.write(dumps(obj))
    return fp


def dumps(obj):
    if inspect.isroutine(obj):
        obj = serialize(obj)

    return qtoml.dumps(obj, encode_none='None')


def load(fp):
    with open(fp, 'r') as f:
        s = f.read()
    return qtoml.loads(s)


def loads(s):
    return deserialize(qtoml.loads(s))
