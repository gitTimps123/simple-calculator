import streamlit as st
from decimal import Decimal, getcontext

# High precision (professional-grade)
getcontext().prec = 28

st.title("Professional Calculator (Accurate)")

num1 = st.text_input("Enter first number", "0")
num2 = st.text_input("Enter second number", "0")

operation = st.selectbox(
    "Choose operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

def calculate(a, b, op):
    a = Decimal(a)
    b = Decimal(b)

    if op == "Add":
        return a + b
    elif op == "Subtract":
        return a - b
    elif op == "Multiply":
        return a * b
    elif op == "Divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

if st.button("Calculate"):
    try:
        result = calculate(num1, num2, operation)
        st.success(f"Result: {result.normalize()}")
    except Exception as e:
        st.error(f"Error: {e}")
