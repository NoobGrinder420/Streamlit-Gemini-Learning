import streamlit as st

counter = 0
col1, col2 = st.columns(2)

with col1:
    if st.button(":arrow_left:"):
        counter -= 1
with col2:
    if st.button(":arrow_right:"):
        counter += 1
        
st.write("Count", counter)



