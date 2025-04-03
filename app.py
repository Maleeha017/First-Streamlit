import streamlit as st
import pandas as pd
st.title("My Streamlit App")

if st.button("Load Data"):
    # Load data from CSV file
    df = pd.read_csv("data.csv")
    st.write(df)