from typing import Protocol

from ._common import Message


class AnyChat(Protocol):
    def read(self) -> Message: ...
    def print(self, msg: Message) -> None: ...


class SimpleChat:
    @staticmethod
    def read() -> Message:
        return Message(input("> "))

    @staticmethod
    def print(msg: Message) -> None:
        print(f"[Bot]\n{msg.text}")


def get_chat() -> AnyChat:
    return SimpleChat
