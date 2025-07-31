from functools import partial
from time import sleep
from typing import Any, Callable, Optional

from requests import Response, get

from .local_cache import request_with_cache
from .request_id import RequestId


def _handle_get(request_id: RequestId) -> Response:
    sleep(1)
    with get(request_id.url, request_id.params) as response:
        response.raise_for_status()
        return response


def get_request(
    name: Optional[str] = None,
    /,
    *exname: str,
    **query: Any,
) -> Response:
    request_id = RequestId(name or "", *exname, **query)
    return request_with_cache(_handle_get, request_id)
