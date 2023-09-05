# -*- coding: utf-8 -*-

from langchain.agents import XMLAgent, tool, AgentExecutor
from langchain.chat_models import ChatAnthropic
from langchain.chains import LLMChain

model = ChatAnthropic(model="claude-2")

@tool
def search(query: str) -> str:
    """Search things about current events."""
    return "32 degrees"

tool_list = [search]

chain = LLMChain(
    llm=model,
    prompt=XMLAgent.get_default_prompt(),
    output_parser=XMLAgent.get_default_output_parser()
)
agent = XMLAgent(tools=tool_list, llm_chain=chain)

agent_executor = AgentExecutor(agent=agent, tools=tool_list, verbose=True)

agent_executor.run("whats the weather in New york?")
