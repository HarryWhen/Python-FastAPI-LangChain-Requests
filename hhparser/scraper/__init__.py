from .local_cache import cache
from .hh_request import get_data


get_data = cache(get_data)


def get_vacancies():
    raise NotImplementedError
