import streamlit as st

st.set_page_config(page_title="SmartCalc", page_icon="🧮")

st.title("🧮 SmartCalc")
st.write("A simple calculator")

num1 = st.number_input("First number", value=0.0)
num2 = st.number_input("Second number", value=0.0)

operation = st.selectbox(
    "Choose an operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (×)":
        result = num1 * num2
    else:
        if num2 == 0:
            st.error("Cannot divide by zero.")
            st.stop()
        result = num1 / num2

    st.success(f"Result: {result}")
