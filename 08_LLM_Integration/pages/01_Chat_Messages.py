import streamlit as st
import pandas as pd

st.chat_message("user").title("I want data :angry:")
        
st.chat_message("assistant").dataframe(
    data={
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"]
    }
)

st.chat_message("user").write("You are a helpful assistant.")

message = st.chat_message("assistant")
if message.toggle(label="toggle me"):
    message.write("slider slided!")
    
    
    
