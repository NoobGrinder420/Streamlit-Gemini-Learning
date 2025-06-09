#Import streamlit for web app
import streamlit as st

# Set the title of the web app
st.title("Toggle Widget")

# Insert a toggle widget
god = st.toggle("Let there be light!")
if god:
   st.write("There is light!")
   st.image("https://files.catbox.moe/azutf3.jpg")
else:
   st.write("I can't see!")