from serialize.serializer import deserialize


def dump(obj, fp):
    s = dumps(obj)
    fp.write(s)


def load(fp):
    return loads(fp.read())


def dumps(obj):
    text = ""
    if isinstance(obj, dict):
        for key, val in obj.items():
            if key == 'dict':
                text += "{"
                text += dumps(val)
                text = text[:-2]
                text += "}"
            elif key == 'list':
                text += '['
                if len(val) != 0:
                    for item in val:
                        if item is None:
                            text += '  '
                            continue
                        else:
                            text += dumps(item) + ', '
                    text = text[:-2]
                text += ']'
            elif key == 'func':
                text += "{"
                text += dumps(key) + ": " + dumps(val) + ', '
                text = text[:-2]
                text += '}'
            elif key == 'code':
                text += "{"
                text += dumps(key) + ": " + '{' + dumps(val)
                text = text[:-2]
                text += '}'
                text += '}'
            elif key == 'bytes':
                text += '{' + dumps(key) + ': ' + dumps(val) + '}'
            else:
                text += dumps(key) + ": " + dumps(val) + ", "

    elif isinstance(obj, str):
        text += '\"' + str(obj) + '\"'

    elif isinstance(obj, int):
        text += str(obj)

    elif isinstance(obj, list):
        if len(obj) != 0:
            for item in obj:
                text += dumps(item) + ', '
            text = text.rstrip(text[-1])
            text = text.rstrip(text[-1])

    return text


def loads(s):
    return deserialize(s)