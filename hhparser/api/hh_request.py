from .local_cache import cache

URI = "https://api.hh.ru"


@cache
def get_data(data_path, data_query):
    raise NotImplementedError
