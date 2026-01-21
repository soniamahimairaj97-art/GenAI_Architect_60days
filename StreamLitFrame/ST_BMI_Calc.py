import streamlit as st

st.set_page_config(page_title="BMI & Unit Tool", page_icon="📏")

st.title("⚖️ Health & Unit Tools")

# Create tabs for different features
tab1, tab2 = st.tabs(["BMI Calculator", "Unit Converter"])

with tab1:
    st.header("BMI Calculator")
    
    # Unit system selection
    unit_system = st.radio("Select System:", ("Metric (kg/cm)", "Imperial (lb/in)"), horizontal=True)

    col1, col2 = st.columns(2)

    with col1:
        if unit_system == "Metric (kg/cm)":
            weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
            # Use CM here for easier user input
            height_cm = st.number_input("Height (cm)", min_value=1.0, value=175.0)
            height_m = height_cm / 100  # Convert to meters for the formula
        else:
            weight = st.number_input("Weight (lb)", min_value=1.0, value=150.0)
            height_in = st.number_input("Height (in)", min_value=1.0, value=68.0)
            height_m = height_in # We handle imperial differently below

    if st.button("Calculate BMI"):
        # Metric Formula
        if unit_system == "Metric (kg/cm)":
            bmi = weight / (height_m ** 2)
        # Imperial Formula
        else:
            bmi = (weight / (height_in ** 2)) * 703

        st.subheader(f"Result: {bmi:.1f}")
        
        # Color-coded status
        if bmi < 18.5:
            st.warning("Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Normal Weight")
        elif 25 <= bmi < 30:
            st.info("Overweight")
        else:
            st.error("Obese")

with tab2:
    st.header("Length Converter")
    st.write("Convert between cm, inches, and meters here!")
    # We can build this next!