from parsers import my_toml
from factory.parsers_factory.abstract_parser import Parser


class Toml(Parser):

    def dump(self, obj, fp):
        return my_toml.dump(obj, fp)

    def dumps(self, obj):
        return my_toml.dumps(obj)

    def load(self, fp):
        return my_toml.load(fp)

    def loads(self, s):
        return my_toml.loads(s)