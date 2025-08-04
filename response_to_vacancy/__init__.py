import dataclasses

from . import ai_agent, simple_chat


@dataclasses.dataclass
class Message:
    text: str


def get_message(*, chat: simple_chat.AnyChat) -> Message:
    return Message(chat.read())


def process(msg: Message, *, agent) -> Message:
    return Message("Даже я не могу разобрать, что ты хочешь")


def reply_with(msg: Message, *, chat: simple_chat.AnyChat) -> None:
    chat.print(msg.text)


def run():
    chat = simple_chat.get_chat()
    agent = ai_agent.get_agent()

    while True:
        prompt = get_message(chat=chat)
        response = process(prompt, agent=agent)
        reply_with(response, chat=chat)
