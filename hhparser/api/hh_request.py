import requests

from .local_cache import cache

URI = "https://api.hh.ru"


@cache
def request_data(data_name="", data_query=None):
    url = f"{URI}/{data_name}"
    params = data_query or {}
    with requests.get(url, params=data_query) as response:
        return response.content.decode()
