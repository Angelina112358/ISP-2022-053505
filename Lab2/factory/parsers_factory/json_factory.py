from parsers import json
from factory.parsers_factory.abstract_parser import Parser
from serialize.serializer import *


class Json(Parser):

    def dump(self, obj, fp):
        return json.dump(obj, fp)

    def dumps(self, obj):
        ser_dict = serialize(obj)
        return json.dumps(ser_dict)

    def load(self, fp):
        return json.load(fp)

    def loads(self, s):
        return json.loads(s)