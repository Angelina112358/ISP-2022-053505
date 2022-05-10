import cmd.argparser
from factory.factory import Factory
from factory.parsers_factory import abstract_parser
from factory.parsers_factory import json_factory
from factory.parsers_factory import toml_factory
from factory.parsers_factory import yaml_factory


load_f, dump_in = cmd.argparser.ArgParser.getargs()


def get_parser(filename: str) -> abstract_parser.Parser:
    ft = filename.lower().split('.')[-1]
    parsers = {
        'json': json_factory.Json,
        'yml': yaml_factory.Yaml,
        'toml': toml_factory.Toml
    }
    return abstract_parser.Parser(parsers.get(ft, None))


def dump(obj, filename: str) -> any:
    parser = get_parser(filename)
    ft = filename.lower().split('.')[-1]
    sr = Factory.create_serializer(ft)
    sr.dump(obj, filename)
    obj = sr.load(filename)

    print('Dump success')
    return obj


def load(filename: str) -> any:
    parser = get_parser(filename)
    sr = Factory.create_serializer()
    item = sr.load(filename)
    print('Load success')
    return item


def convert():
    if load_f is not None:
        obj = load(''.join(load_f))

    if dump_in is not None:
        obj = dump(''.join(dump_in))
