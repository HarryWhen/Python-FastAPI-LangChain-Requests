import functools
import inspect
from typing import Callable, TypeVar

from typing_extensions import ParamSpec

P = ParamSpec("P")
R = TypeVar("R")


def wraps_with_resolver(
    func: Callable[P, R],
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    signature = inspect.signature(func)

    def decorator(wrapper: Callable[P, R]) -> Callable[P, R]:

        @functools.wraps(func)
        def wrapper_with_resolver(*args: P.args, **kwargs: P.kwargs) -> R:
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()
            return wrapper(*bound.args, **bound.kwargs)

        return wrapper_with_resolver

    return decorator
