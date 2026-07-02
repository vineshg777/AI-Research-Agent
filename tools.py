from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_core.tools import tool

load_dotenv()

tavily_tool = TavilySearch(max_results=5, search_depth="advanced")

@tool
def get_topic_summary(topic: str) -> str:
    """Returns a brief overview of a topic using Tavily search."""
    results = tavily_tool.invoke({"query": f"overview of {topic}"})
    return str(results)

@tool
def get_recent_developments(topic: str) -> str:
    """Finds the most recent news and developments on a topic."""
    results = tavily_tool.invoke({"query": f"latest developments in {topic} 2025"})
    return str(results)

@tool
def get_academic_sources(topic: str) -> str:
    """Searches for academic and research sources on a topic."""
    results = tavily_tool.invoke({"query": f"research papers academic sources {topic}"})
    return str(results)

tools = [tavily_tool, get_topic_summary, get_recent_developments, get_academic_sources]