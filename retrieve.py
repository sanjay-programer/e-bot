from langchain_chroma import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from embedding import df
import pandas as pd
import os

current_dir=os.path.dirname(os.path.abspath(__file__))
db_dir=os.path.join(current_dir,"db")
persistent_dir=os.path.join(db_dir,"Data_embeddings")

# print("\n-------creating embeddings---------")
embeddings=HuggingFaceEmbeddings()
# print("\n-----finished creating embeddings------")

db=Chroma(embedding_function=embeddings,persist_directory=persistent_dir)

retriever=db.as_retriever(
    search_type="similarity",
    search_kwargs={"k":6}
)

def query2products(query):
    outputs=retriever.invoke(query)
    lst=[output.page_content for output in outputs]
    return lst

def products_detail(products:list):
    result=[]
    for product in products:
        out=df[df['PRODUCTS']==product]
        result.append(out)
    return pd.concat(result)
