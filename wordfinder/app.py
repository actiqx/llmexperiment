import streamlit as st
import os
from langchain.embeddings import HuggingFaceHubEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()
# Load env will load env from env variables
# os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

#  Page ConFig
st.set_page_config(page_title="Educate Kids",page_icon=":robot:")
st.header("Hey , Ask me something & i will give out similar things")

#initialize the Embeddings
embeddings=HuggingFaceHubEmbeddings()

from langchain.document_loaders.csv_loader import CSVLoader
loader = CSVLoader(file_path="myData.csv",csv_args={
    'delimiter':",",
    'quotechar':'"',
    'fieldnames':['Words']
})

data= loader.load()

print(data)

db =FAISS.from_documents(data,embeddings)

def get_text():
    input_text =st.text_input("You :",key=input)
    return input_text

user_input =get_text()
submit=st.button("Find Similar Things")

if submit:
    docs= db.similarity_search(user_input)
    print(docs)
    st.subheader("Top Matches:")
    st.text(docs[0].page_content)
    st.text(docs[1].page_content)
