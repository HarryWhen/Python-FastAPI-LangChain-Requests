from dataclasses import dataclass

from langchain_ollama import ChatOllama

from ._common import Message


class LLMAgent:
    def __init__(self):
        pass

    def respond_to(self, msg: Message) -> Message:
        return Message("Даже я не могу разобрать, что ты хочешь")


def get_agent() -> LLMAgent:
    return LLMAgent()
