#Import streamlit for web app
import streamlit as st

# Set the title of the web app
st.title("Selectbox Widget")

# Insert a selectbox widget
option = st.selectbox(
  label="Which education level are you currently studying under?",
  options=["Secondary School", "Polytechnic", "Junior College", "University", "Other"]
)
