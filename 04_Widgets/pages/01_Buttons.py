import streamlit as st

# Define a callback function that accepts keyword arguments
def greet(**kwargs):
    name = kwargs.get("name", "Guest")
    st.write(f"Hello, {name}!")

st.button(label="Greet Dhanvin", on_click=greet, kwargs={"name": "Dhanvin"})

if st.button(label="Greet Guest"):
    greet(name="Guest")
    
    