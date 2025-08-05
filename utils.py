import functools
import inspect
import operator
from typing import Callable, Optional, TypeVar, overload

from typing_extensions import ParamSpec

from main import Config

P = ParamSpec("P")
R = TypeVar("R")


@overload
def log(
    *, logger: Callable[[str], None]
) -> Callable[[Callable[P, R]], Callable[P, R]]: ...


@overload
def log(func: Callable[P, R]) -> Callable[P, R]: ...


def log(
    func: Optional[Callable[P, R]] = None,
    *,
    logger: Callable[[str], None] = print,
) -> Callable[[Callable[P, R]], Callable[P, R]] | Callable[P, R]:

    def with_logger(
        func: Callable[P, R],
    ) -> Callable[P, R]:

        @functools.wraps(func)
        def logged(*args: P.args, **kwargs: P.kwargs) -> R:
            logger(f"> call {func.__name__} with {args}, {kwargs}")
            r = func(*args, **kwargs)
            logger(f"< return of {func.__name__} is {r}")
            return r

        return logged if Config.LOG else func

    return with_logger(func) if func else with_logger


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


def report_vacancies(vacancies):
    yield (f"{len(vacancies)} vacancies:")
    yield from map(operator.itemgetter("name"), vacancies)
