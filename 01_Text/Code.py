#Import streamlit for web app
import streamlit as st

st.title("Hello World!")

# Insert some code snippets into our website

code = """
def hello():
   print("Hello there!")
"""


st.code(
    # body kwarg is used for the code string
    body=code,
    
    #language kwarg is used for the programming language
    language="python", 
    
    # line_numbers kwarg is used to display line numbers
    line_numbers=True
)