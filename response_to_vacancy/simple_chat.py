from ._common import Message


class SimpleChat:
    @staticmethod
    def read() -> Message:
        return Message(input(">\t"))

    @staticmethod
    def print(msg: Message) -> None:
        print(f"[Bot]\n\t{msg.text}")
