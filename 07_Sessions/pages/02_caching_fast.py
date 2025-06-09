import streamlit as st
import pandas as pd

@st.cache_data()  # Cache the data for faster loading
def load_data_fast(url):
	df = pd.read_csv(url)  # 👈 Download the data
	return df

df = load_data_fast("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")




