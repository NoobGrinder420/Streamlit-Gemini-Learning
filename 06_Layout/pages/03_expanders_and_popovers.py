import streamlit as st

expander = st.expander(label="Expander", expanded=True)
with expander:
    st.write("This is an expander")
    st.button(label="Click Me", key="expanderbutton")
    expanderinfo = st.text_input(label="Enter some text", key="expanderinput")

popover = st.popover(label="Popover")
with popover:
    st.write("This is a popover")
    st.button(label="Click Me", key="popoverbutton")
    popoverinfo = st.text_input(label="Enter some text", key="popoverinput")
    
popover2 = st.popover(label="Popover", use_container_width=True)
with popover2:
    st.write("This is also a popover")
    st.button(label="Click Me", key="popover2button")
    popover2info = st.text_input(label="Enter some text", key="popover2input")