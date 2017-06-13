from flask import request
from functools import wraps


def convert_json_to(class_):

    def wrap(f):
        @wraps(f)
        def decorator(*args):
            """
            Converts json in object based on class param
            :param args: 
            :return: 
            """
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap