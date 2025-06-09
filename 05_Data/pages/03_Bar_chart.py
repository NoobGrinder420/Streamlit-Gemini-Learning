import streamlit as st
import pandas as pd
import numpy as np

st.title("Bar Chart Example")

# Create sample data
data = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Values": (np.random.randn(3)*10)%10
})

st.bar_chart(data, x="Category", y="Values")


