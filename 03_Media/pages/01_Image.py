#Import streamlit for web app
import streamlit as st

# Insert an image into our website
st.title("Sandwiches!")
st.image(
        #image kwarg is used for image url or file path
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnBlBfoF7g8TUKA3LTBiUYdbvF2rbi1YNeaA&s",
        
        # Use the caption kwarg to add a caption to the image
        # The caption will be displayed below the image
        caption="Sandwiches are the best food!",
        
        # Use the width kwarg to set the width of the image (in px)
        width=300
)

st.image(
        #using a relative file path (absolute also works)
        image="Media/actual media/sandwich.png",

        caption="Sandwiches are pixelated!",
        width=300
)

