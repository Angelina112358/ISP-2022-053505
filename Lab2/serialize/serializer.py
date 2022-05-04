import inspect
import types


def serialize(obj):

    if isinstance(obj, bytes):
        key = "bytes"
        return {key: obj.hex()}

    if isinstance(obj, types.FunctionType):
        return {"func": serialize(obj.__code__)}

    if isinstance(obj, types.CodeType):
        attrs = []
        result = {}
        for member in inspect.getmembers(obj):
            if member[0].startswith('co'):
                attrs.append(member)

        for attr in attrs:
            result[serialize(attr[0])] = serialize(attr[1])

        return {"code": result}

    if isinstance(obj, (int, str, float, bool)):
        return obj

    if isinstance(obj, dict):
        temp = {}
        for key, value in obj.items():
            temp[serialize(key)] = serialize(value)

        return {'dict': temp}

    if isinstance(obj, (tuple, list)):
        temp = []
        for element in obj:
            temp.append(serialize(element))

        return {'list': temp}


def deserialize(obj):
    temp_dict = {}
    if isinstance(obj, (int, str, float)):
        return obj
    elif isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'func':
                import __main__
                globals().update(__main__.__dict__)
                def func(): pass
                func.__code__ = deserialize(value)
                return func
            elif key == 'list':
                return deserialize(value)
            elif key == 'bytes':
                return bytes.fromhex(value)
            elif key == 'code':
                return types.CodeType(
                    deserialize(value["co_argcount"]),
                    deserialize(value["co_posonlyargcount"]),
                    deserialize(value["co_kwonlyargcount"]),
                    deserialize(value["co_nlocals"]),
                    deserialize(value["co_stacksize"]),
                    deserialize(value["co_flags"]),
                    deserialize(value["co_code"]),
                    tuple(deserialize(value["co_consts"])),
                    tuple(deserialize(value["co_names"])),
                    tuple(deserialize(value["co_varnames"])),
                    deserialize(value["co_filename"]),
                    deserialize(value["co_name"]),
                    deserialize(value["co_firstlineno"]),
                    deserialize(value["co_lnotab"]),
                    tuple(deserialize(value["co_freevars"])),
                    tuple(deserialize(value["co_cellvars"]))
                )
            else:
                temp_dict[deserialize(key)] = deserialize(value)

    elif isinstance(obj, list):
        temp_list = []
        for item in obj:
            temp_list.append(deserialize(item))
        return temp_list

    return temp_dict

