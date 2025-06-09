import streamlit as st

st.title("Columns")

col1, col2 = st.columns(spec=2, gap="small")
with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")
   
   
