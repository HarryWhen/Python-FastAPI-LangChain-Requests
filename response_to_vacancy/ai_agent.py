from dataclasses import dataclass
from typing import Callable

from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import create_react_agent

from utils import log

from ._common import Message
from .data_access import get_vacancy_raw_data


def get_prompt() -> str:
    return 'Тебе предстоит анализировать "сырые" данные о вакансиях. Данные '
    "подаются порционно, под одной вакансии. Актуальные данные для анализа "
    "тебе будут доступны сразу, однако чтобы перейти к следующим, тебе "
    "придется делать это самостоятельно. В своих ответах анализируй не "
    "больше одной вакансии за раз. Вакансии не пропускай. Обсуждение одной "
    "вакансии может продолжаться пока пользователь не захочет перейти "
    "дальше. Формат результатов анализа выбирай самостоятельно, однако "
    "старайся, чтобы первый отчет по каждой вакансии был стандартным."


def get_tools() -> tuple[Callable, ...]:
    return (*map(log, [get_vacancy_raw_data]),)


class LLMAgent:

    def __init__(self, agent: CompiledStateGraph) -> None:
        self._agent = agent

    def respond_to(self, msg: Message) -> Message:
        ai_output = self._agent.invoke(
            {
                "messages": [
                    HumanMessage(msg.text),
                ],
            }
        )
        return Message(ai_output["messages"][-1].content)


def get_agent() -> LLMAgent:
    llm = ChatOllama(
        model="llama3.2",
        temperature=0,
    )

    agent = create_react_agent(
        model=llm,
        tools=get_tools(),
        prompt=get_prompt(),
    )

    return LLMAgent(agent)
