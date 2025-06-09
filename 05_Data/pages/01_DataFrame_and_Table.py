import streamlit as st
import pandas as pd

st.title("DataFrames And Tables")

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Display the DataFrame
st.write("Here is a sample DataFrame using st.dataframe():")
st.dataframe(data=df)

# Display the dataframe with a table style
st.write("Here is the same data using st.table():")
st.table(data=data)