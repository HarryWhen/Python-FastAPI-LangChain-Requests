from dataclasses import dataclass

from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import create_react_agent

from ._common import Message


def get_prompt() -> str:
    return ""


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
        tools=[],
        prompt=get_prompt(),
    )

    return LLMAgent(agent)
