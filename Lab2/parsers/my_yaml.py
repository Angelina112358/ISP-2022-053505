from serialize.serializer import deserialize
import yaml


def dump(obj, fp):
    with open(fp, 'w') as f:
        yaml.dump(obj, f)
    return fp
