import streamlit as st

from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
# Load env will load env from env variables
# os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

#  Page ConFig
st.set_page_config(page_title="Prompt",page_icon=":robot:")
st.header("Hey , Create Your tweet")


def load_answer(question):
    wordsCount=20

    llm=HuggingFaceHub(repo_id = "google/flan-t5-xxl")

    our_prompt = f"""
    {question}

    Can you create a post for tweet in {wordsCount} words for the above?
    """
    answer=llm(our_prompt)
    return answer



def get_text():
    input_text =st.text_input("You :",key=input)
    return input_text

user_input =get_text()
response = load_answer(user_input)
submit=st.button("Submit")

if submit:
    st.subheader("Your Tweet:")
    st.text(response)
    
