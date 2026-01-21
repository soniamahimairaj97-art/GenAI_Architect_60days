import streamlit as st

# Title of the app
st.title("🧮 Simple Python Calculator")

# Layout using columns for a cleaner look
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0)
with col2:
    num2 = st.number_input("Enter second number", value=0.0)

# Dropdown for the operation
operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculation logic
result = 0
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Cannot divide by zero! 😒 ")
        result = None

# Display the result
if result is not None:
    st.success(f"### The result is: {result}")