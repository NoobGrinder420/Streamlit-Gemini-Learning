#Import streamlit for web app
import streamlit as st
#Import datetime for date and time manipulation
import datetime

# Set the title of the web app
st.title("Date and Time Widgets")

# Insert a date widget
st.subheader("Date Widget")
date = st.date_input(
    label="Select a date",
    value=datetime.date.today(),
    help="Select a date"
)

# Display the selected date
st.write("Selected date:", date)


# Insert a time widget
st.subheader("Time Widget")
time = st.time_input(
    label="Select a time",
    help="Select a time"
)

# Display the selected time
st.write("Selected time:", time)