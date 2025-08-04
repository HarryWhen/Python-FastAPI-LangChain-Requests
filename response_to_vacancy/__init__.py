from . import _common, ai_agent, simple_chat


def get_message(*, chat: simple_chat.AnyChat) -> _common.Message:
    return chat.read()


def process(msg: _common.Message, *, agent) -> _common.Message:
    return agent.respond_to(msg)


def reply_with(msg: _common.Message, *, chat: simple_chat.AnyChat) -> None:
    chat.print(msg)


def run():
    chat = simple_chat.get_chat()
    agent = ai_agent.get_agent()

    while True:
        prompt = get_message(chat=chat)
        response = process(prompt, agent=agent)
        reply_with(response, chat=chat)
