from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langgraph.prebuilt import create_react_agent
from tools import tools as agent_tools

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model="gpt-4o-mini")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

system_prompt = """
You are a research assistant that will help generate a research paper.
Answer the user query and use necessary tools.
Wrap the output in this format and provide no other text\n{format_instructions}
""".format(format_instructions=parser.get_format_instructions())

agent = create_react_agent(
    model=llm,
    tools=agent_tools,
    prompt=system_prompt
)

query = input("What can I help you research? ")
raw_response = agent.invoke({"messages": [("human", query)]})

try:
    structured_response = parser.parse(raw_response["messages"][-1].content)
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)