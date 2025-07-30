from typing import Any

from requests.compat import urlencode


class RequestId:
    URI = "https://api.hh.ru"

    def __init__(self, *name: str, **query: Any) -> None:
        self.name = "/".join(name)
        self.query = urlencode(query)
        self.url = f"{self.URI}/{self.name}"
        self.params = query
