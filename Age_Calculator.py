import streamlit as st
from datetime import date

st.title("Age Calculator")

today = date.today()

# Input fields for year, month, and day
year = st.number_input("Enter Year of Birth:", min_value=1, max_value=today.year, step=1)
month = st.number_input("Enter Month of Birth:", 1, 12, step=1)
day = st.number_input("Enter Day of Birth:", 1, 31, step=1)

# Button to trigger age calculation
if st.button("Calculate Age"):
    dob = date(int(year), int(month), int(day))  # Convert inputs to integers
    age = (today - dob).days // 365
    st.write("Your age is:", age, "years")
