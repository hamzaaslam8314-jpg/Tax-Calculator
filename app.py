import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Tax Calculator",
    page_icon="💰",
    layout="centered"
)

# ---------------- TAX FUNCTION ----------------
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

    # Surcharge
    if annual_income > 10000000:
        tax = tax * 1.09

    return tax


# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align: center; color: #2E86C1;'>Pakistan Tax Calculator (2025–26)</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    salary_type = st.radio("Salary Type", ["Monthly", "Annual"])

with col2:
    if salary_type == "Monthly":
        monthly_salary = st.number_input("Monthly Salary (PKR)", min_value=0)
        annual_income = monthly_salary * 12
    else:
        annual_income = st.number_input("Annual Salary (PKR)", min_value=0)

# ---------------- CALCULATION ----------------
if annual_income > 0:

    tax = calculate_tax(annual_income)
    monthly_tax = tax / 12
    net_salary = annual_income - tax
    monthly_net = net_salary / 12

    # ---------------- METRICS ----------------
    st.markdown("### 📊 Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Annual Income", f"PKR {annual_income:,.0f}")
    col2.metric("Annual Tax", f"PKR {tax:,.0f}")
    col3.metric("Net Income", f"PKR {net_salary:,.0f}")

    # ---------------- RESULTS ----------------
    st.markdown("### 💡 Detailed Results")

    st.success(f"Monthly Tax: PKR {monthly_tax:,.0f}")
    st.info(f"Monthly Net Salary: PKR {monthly_net:,.0f}")

    # ---------------- CHART ----------------
    data = {
        "Category": ["Income", "Tax", "Net"],
        "Amount": [annual_income, tax, net_salary]
    }

    df = pd.DataFrame(data)
    st.markdown("### 📈 Income vs Tax Breakdown")
    st.bar_chart(df.set_index("Category"))

# ---------------- FOOTER ----------------
st.divider()

st.caption("Disclaimer: This is an estimate based on FY 2025–26 tax slabs. Actual tax may vary based on individual circumstances and company payroll policies.")
