import dataclasses

from . import ai_agent, simple_chat


@dataclasses.dataclass
class Message:
    text: str


def get_prompt(*, chat: simple_chat.AnyChat) -> Message:
    return Message(chat.read())


def respond_to(msg: Message, *, agent) -> Message:
    return Message("Даже я не могу разобрать, что ты хочешь")


def print_msg(msg: Message, *, chat: simple_chat.AnyChat) -> None:
    chat.print(msg.text)


def run():
    chat = simple_chat.get_chat()
    agent = ai_agent.get_agent()

    while True:
        prompt = get_prompt(chat=chat)
        response = respond_to(prompt, agent=agent)
        print_msg(response, chat=chat)
