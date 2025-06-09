import streamlit as st
import pandas as pd

def load_data_slow(url):
	df = pd.read_csv(url)  # 👈 Download the data
	return df

df = load_data_slow("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")


