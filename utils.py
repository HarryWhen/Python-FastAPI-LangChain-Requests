import functools
import inspect


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
