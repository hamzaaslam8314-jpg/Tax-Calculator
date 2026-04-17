
import streamlit as st

def calculate_tax(annual_income):
    tax = 0

    if annual_income <= 600000:
        tax = 0
    elif annual_income <= 1200000:
        tax = (annual_income - 600000) * 0.01
    elif annual_income <= 2200000:
        tax = 6000 + (annual_income - 1200000) * 0.11
    elif annual_income <= 3200000:
        tax = 116000 + (annual_income - 2200000) * 0.23
    elif annual_income <= 4100000:
        tax = 346000 + (annual_income - 3200000) * 0.30
    else:
        tax = 616000 + (annual_income - 4100000) * 0.35

    if annual_income > 10000000:
        tax = tax * 1.09

    return tax


st.title("Pakistan Salary Tax Calculator (2025–26)")

salary_type = st.radio("Select Salary Type:", ["Monthly", "Annual"])

if salary_type == "Monthly":
    monthly_salary = st.number_input("Enter Monthly Salary (PKR)", min_value=0)
    annual_income = monthly_salary * 12
else:
    annual_income = st.number_input("Enter Annual Salary (PKR)", min_value=0)

if annual_income > 0:
    tax = calculate_tax(annual_income)
    monthly_tax = tax / 12
    net_salary = annual_income - tax

    st.subheader("Results")
    st.write(f"Annual Income: PKR {annual_income:,.0f}")
    st.write(f"Annual Tax: PKR {tax:,.0f}")
    st.write(f"Monthly Tax: PKR {monthly_tax:,.0f}")
    st.write(f"Net Annual Income: PKR {net_salary:,.0f}")
