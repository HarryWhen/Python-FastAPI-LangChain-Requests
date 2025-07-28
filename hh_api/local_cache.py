from functools import partial
from pathlib import Path

from utils import build_file_path, wraps_with_resolver

STORAGE_PATH = Path(__file__).parent / ".cache"
INDEX_NAME = "index"
build_file_path = partial(build_file_path, index_name=INDEX_NAME)


class Storage:

    def __init__(self, slot: Path):
        self.slot = slot

    @classmethod
    def get(cls, request_name, request_query):
        return cls(STORAGE_PATH / build_file_path(request_name, request_query))

    def empty(self):
        return not self.slot.exists()

    @property
    def content(self):
        return self.slot.read_text()

    @content.setter
    def content(self, value):
        self.slot.parent.mkdir(parents=True, exist_ok=True)
        self.slot.write_text(value)

    @content.deleter
    def content(self):
        self.slot.unlink()


def cache(request):

    @wraps_with_resolver(request)
    def wrapper(name, query):
        storage = Storage.get(name, query)
        if storage.empty():
            storage.content = request(name, query)
        return storage.content

    return wrapper
