import os
import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_react_agent
from langchain_groq import ChatGroq

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command": "python",
                "args": ["mathserver.py"],
                "transport" : "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport" : "streamable_http",
            }
        }
    )
    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is 3x2 + 2?"}]})
    print(math_response["messages"][-1].content)
asyncio.run(main())