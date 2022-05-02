from factory.parsers_factory.json_factory import Json

PARSERS = {
    "json": Json,
}


class Factory(object):
    @staticmethod
    def create_serializer(file_format: str):
        parser = PARSERS.get(file_format.lower(), None)
        return parser()

