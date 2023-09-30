import streamlit as st

# Function for BB Seed Money
def calculate_bb_seed_money(total_enrollment, allotted_amount):
    bb_seed_money = (total_enrollment * (55/100)) * 2000

    if allotted_amount < bb_seed_money:
        return f"The school has received INR {bb_seed_money - allotted_amount:.2f} less."
    elif allotted_amount == bb_seed_money:
        return "The school has received the appropriate amount."
    elif allotted_amount > bb_seed_money:
        return f"The school has received INR {allotted_amount - bb_seed_money:.2f} more."

# Streamlit App
st.title("BB Seed Money Calculator")

# BB Seed Money Section
st.header("BB Seed Money Calculation")

total_enrollment = st.number_input("Enter Total Enrolment:", min_value=0, step=1)
allotted_amount = st.number_input("Enter the Amount Alloted:", min_value=0, step=1)

if st.button("Calculate"):
    result = calculate_bb_seed_money(total_enrollment, allotted_amount)
    st.write(result)
