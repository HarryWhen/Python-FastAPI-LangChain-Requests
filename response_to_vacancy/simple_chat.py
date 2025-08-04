from typing import Protocol


class AnyChat(Protocol):
    def read(self) -> str: ...
    def print(self, msg: str) -> None: ...


class SimpleChat:
    @staticmethod
    def read() -> str:
        return input("> ")

    @staticmethod
    def print(msg: str) -> None:
        print(f"[Bot]\n{msg}")


def get_chat() -> AnyChat:
    return SimpleChat
