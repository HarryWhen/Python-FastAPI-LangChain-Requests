from pathlib import Path
from functools import wraps


STORAGE_PATH = Path(__file__).parent / ".cache"
INDEX_NAME = "index"


class Storage:

    @staticmethod
    def build_slot(request_path, request_query):
        return STORAGE_PATH / request_path[1:] / (request_query or INDEX_NAME)

    def __init__(self, slot: Path):
        self.slot = slot

    @classmethod
    def get(cls, request_path, request_query):
        return cls(cls.build_slot(request_path, request_query))

    def empty(self):
        return self.slot.exists()

    @property
    def content(self):
        return self.slot.read_text()

    @content.setter
    def content(self, value):
        self.slot.write_text(value)

    @content.deleter
    def content(self):
        self.slot.unlink()


def cache(request):

    @wraps(request)
    def wrapper(path, query):
        storage = Storage.get(path, query)
        if storage.empty():
            storage.content = request(path, query)
        return storage.content

    return wrapper
