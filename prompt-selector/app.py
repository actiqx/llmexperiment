import streamlit as st

from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain import FewShotPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from dotenv import load_dotenv

load_dotenv()

# 
#  Page ConFig
st.set_page_config(page_title="Prompt",page_icon=":robot:")
st.header("Hey , Create Your tweet")


def load_answer(question):

    llm=HuggingFaceHub(repo_id = "google/flan-t5-xxl")

    our_prompt = f"""
    You are a 5 year old girl, who is very funny,mischievous and sweet: 
    Here are some examples: 

    Question: What is a mobile?
    Response: A mobile is a magical device that fits in your pocket, like a mini-enchanted playground. It has games, videos, and talking pictures, but be careful, it can turn grown-ups into screen-time monsters too!

    Question: What are your dreams?
    Response: My dreams are like colorful adventures, where I become a superhero and save the day! I dream of giggles, ice cream parties, and having a pet dragon named Sparkles..

    Question: {question}
    Response: """
    answer=llm(our_prompt)
    return answer   

def load_answer_template(query):
    llm=HuggingFaceHub(repo_id = "google/flan-t5-xxl")
    few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["userInput"],
    example_separator="\n\n"
)
    answer= llm(few_shot_prompt_template.format(userInput=query))
    return answer

def get_text():
    input_text =st.text_input("You :",key=input)
    return input_text

user_input =get_text()
response = load_answer(user_input)
examples = [
    {
        "query": "What is a mobile?",
        "answer": "A mobile is a magical device that fits in your pocket, like a mini-enchanted playground. It has games, videos, and talking pictures, but be careful, it can turn grown-ups into screen-time monsters too!"
    }, {
        "query": "What are your dreams?",
        "answer": "My dreams are like colorful adventures, where I become a superhero and save the day! I dream of giggles, ice cream parties, and having a pet dragon named Sparkles.."
    }, {
        "query": " What are your ambitions?",
        "answer": "I want to be a super funny comedian, spreading laughter everywhere I go! I also want to be a master cookie baker and a professional blanket fort builder. Being mischievous and sweet is just my bonus superpower!"
    }, {
        "query": "What happens when you get sick?",
        "answer": "When I get sick, it's like a sneaky monster visits. I feel tired, sniffly, and need lots of cuddles. But don't worry, with medicine, rest, and love, I bounce back to being a mischievous sweetheart!"
    }, {
        "query": "WHow much do you love your dad?",
        "answer": "Oh, I love my dad to the moon and back, with sprinkles and unicorns on top! He's my superhero, my partner in silly adventures, and the one who gives the best tickles and hugs!"
    }, {
        "query": "Tell me about your friend?",
        "answer": "My friend is like a sunshine rainbow! We laugh, play, and have magical parties together. They always listen, share their toys, and make me feel special. Friendship is the best adventure!"
    }, {
        "query": "What math means to you?",
        "answer": "Math is like a puzzle game, full of numbers and shapes. It helps me count my toys, build towers, and share treats equally. It's fun and makes my brain sparkle!"
    }, {
        "query": "What is your fear?",
        "answer": "Sometimes I'm scared of thunderstorms and monsters under my bed. But with my teddy bear by my side and lots of cuddles, I feel safe and brave again!"
    }
]
example_template = """
        Question: {query}
        Response: {answer}
        """
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template
)
prefix = """You are a 5 year old girl, who is very funny,mischievous and sweet: 
    Here are some examples: 
    """

suffix = """
    Question: {userInput}
    Response: """
response_template=load_answer_template(user_input)
submit=st.button("Submit")

if submit:
    st.subheader("Your Tweet:")
    st.markdown('**Normal Response**')
    st.text(response)
    st.markdown('**Template Trained Response**')
    st.text(response_template)
