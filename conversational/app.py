import streamlit as st

from langchain.llms import HuggingFaceHub

#function to return the response
import os
os.environ['HUGGINGFACEHUB_API_TOKEN']="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"

def load_answer(question):
    llm=HuggingFaceHub(repo_id = "google/flan-t5-large")
    answer=llm(question)
    return answer


#App UI starts here
st.set_page_config(page_title="QA Demo",page_icon=":robot:")
st.header("LangChain demo")

# Get the User Input
def get_text():
    input_text = st.text_input("You :", key="input")
    return input_text

user_input=get_text()
response = load_answer(user_input)

submit = st.button("Generate")

if submit:
    st.subheader("Answer:")
    st.write(response)