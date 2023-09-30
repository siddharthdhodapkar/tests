# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:54:43 2023

@author: lenovo
"""

import streamlit as st
import pandas as pd

# Load data
uploaded_file = st.file_uploader("Choose an Excel file", type=['xls', 'xlsx'])

def analyze_complaints(data):
    df = pd.read_excel(data)
    
    # Table for number of complaints per Zone
    zone_complaints = df.groupby('Zone')['Issue Number'].count().reset_index()
    st.write("Number of Complaints per Zone")
    st.table(zone_complaints)
    
    # Bar chart for Zone-wise complaints
    st.bar_chart(zone_complaints.set_index('Zone'))
    
    # Table for number of complaints per Subcategory
    subcategory_complaints = df.groupby('Subcategory')['Issue Number'].count().reset_index()
    st.write("Number of Complaints per Subcategory")
    st.table(subcategory_complaints)
    
    # Bar chart for Subcategory-wise complaints
    st.bar_chart(subcategory_complaints.set_index('Subcategory'))

if uploaded_file is not None:
    analyze_complaints(uploaded_file)
