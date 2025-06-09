#Import streamlit for web app
import streamlit as st

# Set the title of the web app
st.title("Radio Widget")

# Insert a radio widget
lang = st.radio(
    label="What's your favourite programming language?",
    options=[":rainbow[Python]", "**C++**", "Assembly"],
    captions=["Convenient & concise.", "Lightning-fast :zap:", "Absolutely bare-bones."]
)

if lang == "Assembly":
   st.write("Okay, what's wrong with you?")
else:
   st.write("Good choice!")