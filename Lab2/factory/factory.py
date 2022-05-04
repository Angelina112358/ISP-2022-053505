from .parsers_factory.yaml_factory import Yaml
from .parsers_factory.toml_factory import Toml
from factory.parsers_factory.json_factory import Json

PARSERS = {
    'json': Json,
    'yml': Yaml,
    'toml': Toml
}


class Factory(object):
    @staticmethod
    def create_serializer(file_format: str):
        parser = PARSERS.get(file_format.lower(), None)
        return parser()

