import streamlit as st

st.set_page_config(page_title="Unit Converter App", page_icon="🔄", layout="centered")

# Title
st.title("🔄 Unit Converter App")
st.write("Convert between different units of length and temperature.")

# Conversion functions
def length_conversion(value, from_unit, to_unit):
    conversion_factors = {
        'meters': 1,
        'kilometers': 0.001,
        'feet': 3.28084,
        'inches': 39.3701
    }
    # Convert to meters first
    meters = value / conversion_factors[from_unit]
    # Convert to target unit
    return meters * conversion_factors[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == to_unit:
        return value
    else:
        st.error("Unsupported temperature conversion")
        return None

# Category selection
category = st.selectbox("Select Conversion Category:", ("Length", "Temperature"))

# Input value
value = st.number_input("Enter a value:", min_value=0.0, format="%.2f")

if category == "Length":
    units = ["meters", "kilometers", "feet", "inches"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert Length"):
        result = length_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
    units = ["Celsius", "Fahrenheit"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert Temperature"):
        result = temperature_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
