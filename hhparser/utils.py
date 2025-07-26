import functools
import inspect
import pathlib
import urllib.parse


def wraps_with_resolver(func):
    signature = inspect.signature(func)

    def decorator(wrapper):

        @functools.wraps(func)
        def wrapper_with_resolver(*args, **kwargs):
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()
            return wrapper(*bound.args, **bound.kwargs)

        return wrapper_with_resolver

    return decorator


def build_file_path(request_name, request_query):
    path = request_name or "index"
    if request_query:
        path += f"?{urllib.parse.urlencode(request_query)}"
    return pathlib.PurePath(path)
