from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
import os
from third_parties import LinkedIn
from agents import LinkedInLookupAgent

if __name__ == "__main__":
    load_dotenv()
    open_ai_api_key = os.environ["OPEN_AI_API_KEY"]

    #### Tavily
    linkedin_url = LinkedInLookupAgent.lookup("Dipankar Mitra")
    print(linkedin_url)

    # summary_template = """
    # given the iLinkedIn information {information} anout a person aI want you to create:
    # 1. a short summary
    # 2. few interesting facts about them
    # """
    #
    # summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=open_ai_api_key)
    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # linkedin_data = LinkedIn.scrap_linkedin_profile("", True)
    # res = chain.invoke(input={"information": linkedin_data})
    # print(res)
