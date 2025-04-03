import streamlit as st
import pandas as pd
st.title("My Streamlit App")

if st.button("Load Data"):
    if st.file_uploader("Upload a CSV file", type=["csv"]) is not None:
        # Load data from uploaded CSV file
        df = pd.read_csv(st.file_uploader("Upload a CSV file", type=["csv"]))
        st.write(df)
    else:
        st.warning("Please upload a CSV file to load data.")