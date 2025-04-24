import streamlit as st
# Unit Converter

st.title("Unit Converter")
category =  st.selectbox("Select a category", ["Length", "Weight", "Temperature"])
if category == "Length":
    unit = st.selectbox("Select coversion type", ["m to cm", "cm to m", "km to m", "m to km", "m to mm", "mm to m"])
elif category == "Weight":
    unit = st.selectbox("Select conversion type", ["kg to g", "g to kg", "g to mg", "mg to g", "kg to mg","mg to kg"])
elif category == 'Temperature':
    unit = st.selectbox("Select conversion type", ["C to F", "F to C", "C to K", "K to C", "F to K", "K to F"])
def convert_units(value, unit):
    if unit == "m to cm":
        result = value * 100
        return result
    elif unit == "cm to m":
        result = value / 100
        return result
    elif unit == "km to m":
        result = value * 1000
        return result
    elif unit == "m to km":
        result =value/1000
        return result
    elif unit == "m to mm":
        result = value * 1000
        return result
    elif unit == "mm to m":
        result =value/1000
        return result
    elif unit == "kg to g":
        result = value * 1000
        return result
    elif unit == "g to kg":
        result = value / 1000
        return result
    elif unit == "g to mg":
        result = value * 1000
        return result
    elif unit == "mg to g":
        result = value / 1000 
        return result
    elif unit == "kg to mg":
        result = value * 1000000
        return result
    elif unit == "mg to kg":
        result = value / 1000000
        return result
    elif unit == "C to F":
        result = (value * (9/5)) + 32
        return result
    elif unit == "F to C":
        result = (value - 32) * 5/9
        return result
    elif unit == "C to K":
        result = value + 273.15 
        return result
    elif unit == "K to C":
        result = value -273.15
        return result
    elif unit == "F to K":
        result = (value - 32) * 5/9 +273.15
        return result
    elif unit == "K to F":
        result = (value -273.15) * 9/5 + 32
        return result
    else:
        return 0

value = st.number_input("Enter the value to convewrt")
if st.button("Convert"):
    result = convert_units(value, unit)
    st.success(f"The converted value is {result}")