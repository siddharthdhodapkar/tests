import streamlit as st
import pandas as pd
import subprocess

# Check if openpyxl is installed, if not, install it
try:
    import openpyxl
except ImportError:
    st.write("Installing openpyxl...")
    subprocess.run(["pip", "install", "openpyxl"])
    st.write("openpyxl installed successfully!")

# Function to analyze complaints
def analyze_complaints(data):
    df = pd.read_excel(data)
    zone_complaints = df.groupby('Zone')['Issue Number'].count().reset_index()
    subcategory_complaints = df.groupby('Subcategory')['Issue Number'].count().reset_index()
    return zone_complaints, subcategory_complaints

# Streamlit UI
st.title("Complaints Analysis")

# File upload
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

# If file is uploaded
if uploaded_file is not None:
    # Analyze complaints
    zone_data, subcategory_data = analyze_complaints(uploaded_file)

    # Display zone data
    st.subheader("Complaints by Zone")
    st.write(zone_data)

    # Display subcategory data
    st.subheader("Complaints by Subcategory")
    st.write(subcategory_data)

    # Add code for bar charts here
