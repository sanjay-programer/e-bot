from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import pandas as pd
import os

current_dir=os.path.dirname(os.path.abspath(__file__))
db_dir=os.path.join(current_dir,"db")
persistent_dir=os.path.join(db_dir,"Data_embeddings")

#getting dataset
df=pd.read_csv("products.csv")
products_names=df["PRODUCTS"].tolist()


if not os.path.exists(persistent_dir):
    print("\n initializing vector database .. ")

    #creating embeddings
    print("\n-----creating embeddings-----")
    embeddings = HuggingFaceEmbeddings()
    print("\n-----Finished creating embeddings-------")

    #checking if file exists
    if not products_names:
        raise FileNotFoundError("file not found")

    print("\n----initializing vector stores-------")
    db=Chroma.from_texts(products_names,embedding=embeddings,persist_directory=persistent_dir)
    print("\n-----finished storing vectors--------")