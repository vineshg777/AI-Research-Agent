# AI Research Agent

An agentic research assistant that takes a natural language query, searches the web and returns a structured research summary with real sources.
Built this as my first end-to-end AI agent to get hands-on with LangChain, LangGraph and tool calling coming from theory to actually building something that works was the goal.

## What it does

- Takes a user query via the terminal
- Uses three Tavily powered search tools to find topic overviews, recent developments and academic sources
- Returns a structured JSON response parsed into a Pydantic model

## Tech Stack

- Python
- LangChain + LangGraph
- OpenAI GPT-4o-mini
- Tavily Search API
- Pydantic

## Setup

1. Clone the repo
2. Create a virtual environment and install dependencies

```bash
pip install langchain langgraph langchain-openai langchain-tavily python-dotenv pydantic
```

3. Create a `.env` file with your API keys
