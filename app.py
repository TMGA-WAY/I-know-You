from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
import os
from third_parties import LinkedIn

if __name__ == "__main__":
    load_dotenv()
    open_ai_api_key = os.environ["OPEN_AI_API_KEY"]
    response = LinkedIn.scrap_linkedin_profile("", True)
    for item in response:
        print(item)

    # information = """
    # Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; owner, executive chairman, and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is one of the wealthiest people in the world; as of April 2024, Forbes estimates his net worth to be $178 billion.[4]
    #
    # A member of the wealthy South African Musk family, Musk was born in Pretoria and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University, but dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999. That same year, Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal. In October 2002, eBay acquired PayPal for $1.5 billion. Using $100 million of the money he made from the sale of PayPal, Musk founded SpaceX, a spaceflight services company, in 2002.
    #
    # """
    #
    # summary_template = """
    # given the information {information} anout a person aI want you to create:
    # 1. a short summary
    # 2. few interesting facts about them
    # """
    #
    # summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=open_ai_api_key)
    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # res = chain.invoke(input={"information": information})
    # print(res)