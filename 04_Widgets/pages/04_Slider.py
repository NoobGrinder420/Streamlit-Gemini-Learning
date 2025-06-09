#Import streamlit for web app
import streamlit as st

# Set the title of the web app
st.title("Slider Widget")

# Insert a slider widget
score = st.slider(
    label="What's your exam score?", 
    
    min_value=0, 
    max_value=100, 
                  
    value=50, 
    step=1
)

# Pass logic
if score >= 50:
    st.write("You're such a brainiac!")
else:
    st.write("Erm... what the sigma?")
    
    
    
# Insert a slider widget with a range
value_range = st.slider(
    label="Select a range of values", 
    
    min_value=0, 
    max_value=100, 
    
    value=(25, 75), 
    step=5
)

# Display the selected range
st.write(f"Selected range: {value_range[0]} to {value_range[1]}")

# Range logic
st.write(
    f'''
    Your exam score is\
    {'' if value_range[0] <= score <= value_range[1] else 'not '}\
    within the selected range
    '''
)