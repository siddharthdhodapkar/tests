# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:46:01 2023

@author: lenovo
"""

import streamlit as st
import pandas as pd

# Function to perform the analysis
def analyze_complaints(data):
    df = pd.read_excel(data)
    
    # Create a pivot table to aggregate data
    pivot_table = df.pivot_table(index='Zone', columns='Status Name', aggfunc='size', fill_value=0)
    
    # Calculate required metrics
    pivot_table['Total Complaints'] = pivot_table.sum(axis=1)
    pivot_table['Short Term Complaints'] = pivot_table['No Action Taken'] + pivot_table['Resolved'] + pivot_table['Submitted for Approval']
    pivot_table['Large Scale Project'] = pivot_table['Large Scale Project']
    pivot_table['Pendency%'] = ((pivot_table['Large Scale Project'] + pivot_table['No Action Taken'] + pivot_table['Submitted for Approval']) / pivot_table['Total Complaints']) * 100
    
    return pivot_table

# Streamlit app
st.title("Complaints Analysis")

# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file is not None:
    # Perform analysis
    result = analyze_complaints(uploaded_file)
    
    # Display result
    st.write("Analysis Result:")
    st.write(result)
