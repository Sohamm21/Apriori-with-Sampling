import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules
import time

st.markdown("""
    <style>
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #000000;
        }
        ::-webkit-scrollbar-thumb {
            background: #A020F0;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #555;
        }
        
        /* Center text */
        .centered {
            display: flex;
            justify-content: center;
            text-align: center;
    </style>
""", unsafe_allow_html=True)
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown('<h1 class="centered">Apriori using Sampling</h1>', unsafe_allow_html=True)
# st.title("Apriori using Sampling")

file_type = st.radio("Select the type of file:", ["CSV", "XLS"])

file_uploaded = 0
if file_type == "CSV":
    st.write("***Upload your dataset in csv format:***")
    file = st.file_uploader("Choose a CSV file", type="csv")
elif file_type == "XLS":
    st.write("***Upload your dataset in XLS format:***")
    file = st.file_uploader("Choose a XLS file", type="xls")
    
if (file is not None) and (file_type == "CSV"):
    df = pd.read_csv(file)
    st.dataframe(df.head())
    file_uploaded = 1
elif (file is not None) and (file_type == "XLS"):
    df = pd.read_excel(file)
    st.dataframe(df.head())
    file_uploaded = 1
else:
    st.warning("Please upload a file.")
    
if file_uploaded == 1:
    data_type = st.radio("Is the data in binary form:", ["Yes", "No"])
    if data_type == "No":
        num_data = pd.get_dummies(df)
        sample_size = st.number_input("Enter the sample size: ", value=0, step=100, format="%d")
        sample_df = num_data.sample(n=sample_size, random_state=42)
    else:
        df.replace({True: 1, False: 0}, inplace=True)
        drop = st.radio("Do you want to drop any column?", ["Yes", "No"])
        if drop == "Yes":
            column_to_drop = st.selectbox('Select a column to drop:', df.columns)
            df = df.drop(columns=[column_to_drop])
        sample_size = st.number_input("Enter the sample size: ", value=0, step=100, format="%d")
        sample_df = df.sample(n=sample_size, random_state=42)
    st.dataframe(sample_df.head())
    
    min_sup = st.number_input("Enter the minimum support: ", format="%.3f")
    
    frequent_items = apriori(sample_df, min_support = min_sup, use_colnames = True)
    frequent_items_df = pd.DataFrame(frequent_items)
    st.dataframe(frequent_items_df, height = 500, width = 1000)