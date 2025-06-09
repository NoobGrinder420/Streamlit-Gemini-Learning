import streamlit as st

st.chat_message("ai").write("What is your name?")

if user_input := st.chat_input(placeholder="Type your message here..."):
    st.chat_message("user").write(user_input)
    st.chat_message("ai").write(f"Hi {user_input}, how can I assist you today?")
    

    
    
    
    
    