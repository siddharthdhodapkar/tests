import streamlit as st

# Salary Increment Code
def calculate_increment(current_salary, years_remaining, increment_percent):
    new_salary = current_salary
    for _ in range(years_remaining):
        new_salary += new_salary * (increment_percent / 100)
    return new_salary

# Streamlit App
st.title("Salary Increment Calculator")

# Input fields
current_salary = st.number_input("Enter Current Salary:", min_value=0.0)
years_remaining = st.number_input("Enter the Number of Years Remaining in Service:", min_value=0, step=1)
increment_percent = st.number_input("Enter the Desired Increment:", min_value=0.0, max_value=100.0, step=0.01)

# Calculate increment
if st.button("Calculate Increment"):
    new_salary = calculate_increment(current_salary, years_remaining, increment_percent)
    st.write(f"The new salary after {years_remaining} years will be: {new_salary}")