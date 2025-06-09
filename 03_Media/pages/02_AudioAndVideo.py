#Import streamlit for web app
import streamlit as st

st.title("Meet the Italian Brainrots!")

# Insert an audio into our website
st.subheader("gegagedigedagedago")
st.audio(
    # data kwarg is used for audio url or file path
    data="Media/actual media/gegagedigedagedago.mp3", 
    
    start_time=0,
    end_time=None,
    
    autoplay=False,
    loop=True
)

st.subheader("italian brainrot")
st.video(
    # data kwarg is used for video url or file path
    data="Media/actual media/brainrot.mp4",
    
    start_time=0,
    end_time=None,
    
    autoplay=True,
    loop=False
)   