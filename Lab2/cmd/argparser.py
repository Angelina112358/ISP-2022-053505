import argparse


class ArgParser:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-l', '--load', dest='l')
        parser.add_argument('-d', '--dump', dest='d')
        parser.add_argument('-c', '--config', dest='c')
        return parser.parse_args()

    @staticmethod
    def load_f() -> list[str]:
        args = ArgParser.parse()
        return args.l

    @staticmethod
    def dump_in() -> list[str]:
        args = ArgParser.parse()
        return args.d

    @staticmethod
    def getargs():
        args = ArgParser.parse()
        return args.l, args.d

    @staticmethod
    def get_config(config: str) ->list[str]:
        try:
            file = open(config, 'r')
            configs = file.read()
        except Exception as e:
            print(e)
        finally:
            file.close()
            return configs.split('\n')

