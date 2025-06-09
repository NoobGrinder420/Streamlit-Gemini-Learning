#Import streamlit for web app
import streamlit as st

# Set the title of the web app
st.title("Checkbox Widget")

# Insert a checkbox widget
agree = st.checkbox("I agree to the terms & conditions.")
if agree:
    st.write("Great!")
    
st.write("Real or fake?")


