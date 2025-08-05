from . import ai_agent, simple_chat


def run():
    chat = simple_chat.get_chat()
    agent = ai_agent.get_agent()

    while True:
        prompt = chat.read()
        response = agent.respond_to(prompt)
        chat.print(response)
