import streamlit as st
#from math import sin, cos
import numpy as np
import pandas as pd

st.title("Line Charts")

# Create a sample dataset
x = np.arange(-100, 100) / 10 # 0.0 to 10.0  
y1 = np.sin(x)                               
y2 = np.cos(x)                               

## [i/10 for i in range(0, 100)]
## [sin(i/10) for i in range(0, 100)]
## [cos(i/10) for i in range(0, 100)]

dataset = {
    'x value': x,
    'sin(x)': y1,
    'cos(x)': y2,
}

# Display the dataset
st.dataframe(data=dataset)


# Create the line chart
st.line_chart(
    data=dataset, 
    
    x="x value",
    y=["sin(x)", "cos(x)"],
    
    x_label="x value",
    y_label="f(x) value",
    
    color=["#0000FF", "#FF0000"]
    
) 


