from parsers import my_yaml
from factory.parsers_factory.abstract_parser import Parser


class Yaml(Parser):

    def dump(self, obj, fp):
        return my_yaml.dump(obj, fp)

    def dumps(self, obj):
        return my_yaml.dumps(obj)

    def load(self, fp):
        return my_yaml.load(fp)

    def loads(self, s):
        return my_yaml.loads(s)