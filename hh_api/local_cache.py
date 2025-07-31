from pathlib import Path
from pickle import dumps, loads
from typing import Callable, Self

from requests import Response

from main import Config

from .request_id import RequestId

STORAGE_PATH: Path = Path(__file__).parent / ".cache"
INDEX_NAME: str = "index"


def build_file_path(request_id: RequestId) -> Path:
    return STORAGE_PATH / request_id.name / (request_id.query or INDEX_NAME)


class Storage:

    def __init__(self, cache_file: Path) -> None:
        self._file: Path = cache_file

    @classmethod
    def get(cls, request_id: RequestId) -> Self:
        return cls(build_file_path(request_id))

    def empty(self) -> bool:
        return not self._file.exists()

    @property
    def response(self) -> Response:
        return loads(self._file.read_bytes())

    @response.setter
    def response(self, value: Response) -> None:
        self._file.parent.mkdir(parents=True, exist_ok=True)
        self._file.write_bytes(dumps(value))
        if Config.DEBUG:
            self._file.with_suffix(".json").write_text(value.content.decode())

    @response.deleter
    def response(self) -> None:
        self._file.unlink()


def request_with_cache(
    request_call: Callable[[RequestId], Response],
    request_id: RequestId,
) -> Response:
    storage = Storage.get(request_id)
    if storage.empty():
        storage.response = request_call(request_id)
    return storage.response
