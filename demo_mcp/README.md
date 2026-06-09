# Demo MCP (Model Context Protocol)

A demo project showcasing how to build and connect MCP servers with a LangGraph ReAct agent powered by Groq.

## Project Structure

```
demo_mcp/
├── mathserver.py    # MCP server exposing math tools (add, multiply) via stdio
├── weather.py       # MCP server exposing a weather tool via HTTP
├── client.py        # LangGraph agent that connects to both MCP servers
└── main.py          # Entry point placeholder
```

## How It Works

- `mathserver.py` — FastMCP server with `add` and `multiply` tools, running over `stdio`
- `weather.py` — FastMCP server with a `get_weather` tool, running over `streamable-http` on `http://localhost:8000/mcp`
- `client.py` — Uses `MultiServerMCPClient` to connect to both servers, loads tools, and runs a `qwen-qwq-32b` ReAct agent via Groq

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file:
   ```
   GROQ_API_KEY=<your_groq_api_key>
   ```

3. Start the weather server:
   ```bash
   python weather.py
   ```

4. Run the agent:
   ```bash
   python client.py
   ```

## Dependencies

- `mcp` — Model Context Protocol SDK
- `langchain-mcp-adapters` — LangChain adapters for MCP
- `langgraph` — ReAct agent framework
- `langchain-groq` — Groq LLM integration
