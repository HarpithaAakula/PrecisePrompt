# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
# added code from here
# from IPython.display import display
# from IPython.display import Markdown

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



def to_markdown(text):
    # Replace bullet points with markdown bullet points
    text = text.replace('•', '*')
    # Indent the text with markdown blockquote style
    text = textwrap.indent(text, '> ')
    # Display the text as markdown
    st.markdown(text, unsafe_allow_html=True)


# added code till here

import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response1(input,image):
    model1 = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response1 = model.generate_content([input,image])
    else:
       response1 = model.generate_content(image)
    return response1.text

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text





##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Ask the question")
submit1=st.button("Ask about the image")

## If ask button is clicked
if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)

if submit1:
    
    response1=get_gemini_response1(input,image)
    st.subheader("The Response is")
    st.write(response)