import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])

container = st.container(border=True)
with container:
    st.write("This is inside the container")   
    st.bar_chart(data=df)

st.write("This is outside the container")


