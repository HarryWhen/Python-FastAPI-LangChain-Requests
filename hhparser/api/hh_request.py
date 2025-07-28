import json
import time

import requests

from .local_cache import cache

URI = "https://api.hh.ru"


@cache
def _request_data(data_name, data_query):
    url = f"{URI}/{data_name}"
    time.sleep(1)
    with requests.get(url, params=data_query) as response:
        return response.raise_for_status() or response.content.decode()


def request_data(data_name="", data_query={}):
    return json.loads(_request_data(data_name, data_query))


def _request_vacancies(*, text, experience, excluded_text, **kwargs):
    query = {
        "text": text,
        "experience": experience,
        "excluded_text": excluded_text,
        **kwargs,
    }
    return request_data("vacancies", query)


def request_vacancies(*, page, per_page, text, experience, excluded_text):
    return _request_vacancies(**locals(), order_by="relevance", no_magic=True)


def request_vacancies_statistics(*, text, experience, excluded_text):
    return _request_vacancies(**locals(), per_page=0, clusters=True)
