from . import _common, ai_agent


def get_prompt(*, chat) -> _common.Message:
    raise NotImplementedError()


def respond_to(msg: _common.Message, *, agent) -> _common.Message:
    raise NotImplementedError()


def print_msg(msg: _common.Message, *, chat) -> _common.Message:
    raise NotImplementedError()


def run():
    chat = get_chat()
    agent = get_agent()

    while True:
        prompt = get_prompt(chat=chat)
        response = respond_to(prompt, agent=agent)
        print_msg(response, chat=chat)
