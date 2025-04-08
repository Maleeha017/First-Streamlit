import streamlit as st
import pandas as pd
st.title("My Streamlit App")

if st.button("Load Data"):
    if st.file_uploader("Upload a CSV file", type=["csv"]) is not None:
        # Load data from uploaded CSV file
        df = pd.read_csv(st.file_uploader("Upload a CSV file", type=["csv"]))
        if df is not None:
            st.write("Data loaded successfully!")
            st.dataframe(df)

api_key = st.secrets["alpha_vantage"]["api_key"]
st.write("API Key:", api_key)