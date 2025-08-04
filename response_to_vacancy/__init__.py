import dataclasses

from . import ai_agent


@dataclasses.dataclass
class Message:
    text: str


def get_prompt(*, chat) -> Message:
    raise NotImplementedError()


def respond_to(msg: Message, *, agent) -> Message:
    raise NotImplementedError()


def print_msg(msg: Message, *, chat) -> Message:
    raise NotImplementedError()


def run():
    chat = get_chat()
    agent = get_agent()

    while True:
        prompt = get_prompt(chat=chat)
        response = respond_to(prompt, agent=agent)
        print_msg(response, chat=chat)
