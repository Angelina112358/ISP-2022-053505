from parsers import my_json
from factory.parsers_factory.abstract_parser import Parser
from serialize.serializer import serialize


class Json(Parser):

    def dump(self, obj, fp):
        s = serialize(obj)
        return my_json.dump(s, fp)

    def dumps(self, obj):
        s = serialize(obj)
        return my_json.dumps(s)

    def load(self, fp):
        return my_json.load(fp)

    def loads(self, s):
        return my_json.loads(s)