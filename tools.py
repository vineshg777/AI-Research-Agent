from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from datetime import datetime

load_dotenv()

tavily_tool = TavilySearch(max_results=5, search_depth="advanced")

@tool
def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """Saves research output to a text file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"

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

tools = [tavily_tool, get_topic_summary, get_recent_developments, get_academic_sources, save_to_txt]