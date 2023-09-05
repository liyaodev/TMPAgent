# -*- coding: utf-8 -*-

import os
os.environ["LANGCHAIN_TRACING"] = "true" # If you want to trace the execution of the program, set to "true"

from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent

from langchain.agents.agent_toolkits import PlayWrightBrowserToolkit
from langchain.tools.playwright.utils import (
    create_async_playwright_browser,
    create_sync_playwright_browser, # A synchronous browser is available, though it isn't compatible with jupyter.
)

# This import is required only for jupyter notebooks, since they have their own eventloop
import nest_asyncio
nest_asyncio.apply()

async_browser = create_async_playwright_browser()
browser_toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
tools = browser_toolkit.get_tools()

llm = ChatOpenAI(temperature=0) # Also works well with Anthropic models
agent_chain = initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

response = await agent_chain.arun(input="Hi I'm Erica.")
print(response)


response = await agent_chain.arun(input="Don't need help really just chatting.")
print(response)

response = await agent_chain.arun(input="Browse to blog.langchain.dev and summarize the text, please.")
print(response)

response = await agent_chain.arun(input="What's the latest xkcd comic about?")
print(response)

# from langchain.prompts import MessagesPlaceholder
# from langchain.memory import ConversationBufferMemory
# chat_history = MessagesPlaceholder(variable_name="chat_history")
# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# agent_chain = initialize_agent(
#     tools, 
#     llm, 
#     agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
#     verbose=True, 
#     memory=memory, 
#     agent_kwargs = {
#         "memory_prompts": [chat_history],
#         "input_variables": ["input", "agent_scratchpad", "chat_history"]
#     }
# )
# response = await agent_chain.arun(input="Hi I'm Erica.")
# print(response)
# response = await agent_chain.arun(input="whats my name?")
# print(response)
