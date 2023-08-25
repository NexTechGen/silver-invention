import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streemlit by Rusaid")

st.header("Hello Ruzait")

st.subheader("Input Widgets in Streamlit")

data = pd.read_csv("iris.csv")
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

cols = list(data.columns)

col1, col2 = st.columns(2)

with col1:
    a =  st.slider("Enter a number one:", 0, 100, 10)

with col2:
    b =  st.slider("Enter a number two:", 0, 10, 1)


submit = st.checkbox("Add")

if submit:
    st.write("The Sum of number one and number two:", a+b)

    option = st.multiselect("Choose multy select", cols)

    st.write("your select", option)