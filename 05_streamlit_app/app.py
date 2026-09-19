import streamlit as st
import pandas as pd
import os

from data_processing import run_data_pipeline

st.header("Upload Healthcare Dataset")

uploaded_file = st.file_uploader("Upload your File",type=["csv"])

if uploaded_file is not None:
    st.success("File Uploaded Successfully")

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded file")
    st.dataframe(df)

    if st.button("Process Data"):
        raw_file_path = "../01_Dataset/01_raw/Heart_raw_uncleaned.csv"

        with open(raw_file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        st.info("Running data processing notebooks...")

        run_data_pipeline()

        st.success("✅ Data processing completed!")