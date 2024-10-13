from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from retrieve import products_detail,query2products
from dotenv import load_dotenv
import os

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash")

system_template="""Hey,you are an e-commerce chat bot. you are build to answer user query based on the data you have retrieved which is pandas dataframe
    data:{data}
    
    you will extract the data and try to answer user queries by understanding them
    if user question is irrelevant to e-commerce application then reply i can't answer this question 
    if user question is relevant to e-commerce application but cannot be answered due to insufficient data or irrelevant data then reply i don't know
    you need to complete the conversation in one go you cannot continue the conversation .. i.e you won't have chat history
    Answer in a professional way . don't add extra symbols or stars in the reply let it be professional answer
"""

message=[
    ("system",system_template),
    ("human","{query}")
]

query="Hey i want to go for wedding do you have anything for me ??"

# output=products_detail(query2products(query))
# print(output)
#
prompt=ChatPromptTemplate.from_messages(message)
# out=prompt.invoke({"data":output,"query":query},)

def user_chat(query):
    chain=prompt|llm|StrOutputParser()
    data=products_detail(query2products(query))
    output=chain.invoke({"data":data,"query":query})
    return output

print(user_chat(query))