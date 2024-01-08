import streamlit as st

from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()
output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()

#  Page ConFig
st.set_page_config(page_title="Prompt",page_icon=":robot:")
st.header("Hey , Search Similar Type")


def load_answer(question):

    llm=HuggingFaceHub(repo_id = "google/flan-t5-xxl")

    prompt = PromptTemplate(
    template = "Provide 10 distinct examples of {query}.\n{format_instructions}",
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions}
)
    prompt=prompt.format(query=question)
    answer=llm(prompt)
    return answer

def get_text():
    input_text =st.text_input("You :",key=input)
    return input_text

user_input =get_text()
response = load_answer(user_input)

submit=st.button("Submit")

if submit:
    st.subheader(f"""Provide 5 examples of {user_input}:""")
    st.markdown('**Normal Response**')
    st.text(response)
   
