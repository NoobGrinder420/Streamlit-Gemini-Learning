#Import streamlit for web app
import streamlit as st

# Set the title of the web app
st.title("Text Input Widget")

# Insert a textinput widget
goal = st.text_input("Daily goal", "touch some grass")

# Display the text input
st.write(f"Your goal for today is to {goal}.")
