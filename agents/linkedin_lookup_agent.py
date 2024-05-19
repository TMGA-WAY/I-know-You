import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools import TavilyTools

load_dotenv()



class LinkedInLookupAgent:
    @staticmethod
    def lookup(name: str) -> str:
        open_ai_api_key = os.environ["OPEN_AI_API_KEY"]
        print(open_ai_api_key)
        tavily_api_key = os.environ["TAVILY_API_KEY"]
        llm = ChatOpenAI(temperature=0,
                         model_name='gpt-3.5-turbo',
                         openai_api_key=open_ai_api_key)

        template = """ given the full name {name_of_person}, I want you to get it me a link to their linkedin profile
                    page. Your Answer should contain only a URL.
                    """
        prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])
        tools_for_agent = [
            Tool(name="Crawl google 4 linkedin profile page",
                 func=TavilyTools.get_profile_url_tavily,
                 description="useful for when you need to get the linkedin page url",)
        ]

        react_prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

        result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=name)})

        linkedin_profile_url = result.get("output")
        return linkedin_profile_url
