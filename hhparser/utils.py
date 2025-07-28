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


def build_file_path(request_name, request_query, *, index_name):
    file_name = urllib.parse.urlencode(request_query) if request_query else index_name
    path = f"{request_name}/{file_name}" if request_name else file_name
    return pathlib.PurePath(path)
