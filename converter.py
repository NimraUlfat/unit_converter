import streamlit as st

# Function to convert units
def convert_units(value, from_unit, to_unit, conversion_type):
    conversion_dict = {
        "Distance": {
            "meters": 1,
            "kilometers": 0.001,
            "centimeters": 100,
            "millimeters": 1000,
            "nanometers": 1000000000,
            "miles": 0.000621371,
            "yards": 1.09361,
            "feet": 3.28084,
            "inches": 39.3701,
            "nautical miles": 0.000539957,
        },
        "Weight": {
            "grams": 1,
            "kilograms": 0.001,
            "milligrams": 1000,
            "pounds": 0.00220462,
            "ounces": 0.035274,
        },
        "Temperature": {
            "Celsius": lambda x: x,
            "Fahrenheit": lambda x: x * 9/5 + 32,
            "Kelvin": lambda x: x + 273.15,
        },
        "Frequency": {
            "Hz": 1,
            "kHz": 0.001,
            "MHz": 0.000001,
            "GHz": 0.000000001,
        },
        "Area": {
            "square meters": 1,
            "square kilometers": 0.000001,
            "square centimeters": 10000,
            "square millimeters": 1000000,
            "square miles": 3.861e-7,
            "square yards": 1.19599,
            "square feet": 10.7639,
            "square inches": 1550.0031,
        },
        "Data Transfer Rate": {
            "bps": 1,
            "kbps": 0.001,
            "mbps": 0.000001,
            "gbps": 0.000000001,
            "tbps": 0.000000000001,
        },
        "Digital Storage": {
            "bytes": 1,
            "kilobytes": 0.0009765625,
            "megabytes": 9.5367431640625e-7,
            "gigabytes": 9.313225746154785e-10,
            "terabytes": 9.094947017729282e-13,
        },
        "Energy": {
            "joules": 1,
            "kilojoules": 0.001,
            "calories": 0.239006,
            "kilocalories": 0.000239006,
            "watt-hours": 0.000277778,
        },
        "Fuel Economy": {
            "mpg (US)": 1,
            "mpg (UK)": 1.20095,
            "L/100km": 235.214583,
            "km/L": 2.35215,
        },
        "Plane Angle": {
            "radians": 1,
            "degrees": 57.2958,
            "gradians": 63.661977,
        },
        "Pressure": {
            "pascal": 1,
            "kilopascal": 0.001,
            "bar": 0.00001,
            "atm": 9.86923e-6,
            "mmHg": 0.00750062,
            "psi": 0.000145038,
        },
        "Speed": {
            "m/s": 1,
            "km/h": 3.6,
            "mph": 2.23694,
            "knots": 1.94384,
        },
        "Time": {
            "seconds": 1,
            "minutes": 1/60,
            "hours": 1/3600,
            "days": 1/86400,
            "weeks": 1/604800,
            "months": 1/2629746,
            "years": 1/31556952,
        },
        "Volume": {
            "liters": 1,
            "milliliters": 1000,
            "cubic meters": 0.001,
            "cubic centimeters": 1000,
            "cubic inches": 61.0237,
            "gallons (US)": 0.264172,
            "gallons (UK)": 0.219969,
            "quarts (US)": 1.05669,
            "quarts (UK)": 0.879876,
        }
    }

    # Unit conversion logic
    if conversion_type in conversion_dict:
        if conversion_type == "Distance" or conversion_type == "Weight" or conversion_type == "Area" or conversion_type == "Speed" or conversion_type == "Volume":
            converted_value = value * conversion_dict[conversion_type][to_unit] / conversion_dict[conversion_type][from_unit]
        elif conversion_type == "Time":
            converted_value = value * conversion_dict["Time"][to_unit] / conversion_dict["Time"][from_unit]
        else:
            converted_value = value * conversion_dict[conversion_type][to_unit]
    
    return round(converted_value, 4)

# Streamlit UI
st.set_page_config(page_title="Unit Converter 🔄", page_icon="🔄", layout="wide")


st.title("Unit Converter 🔄")

# Initialize session state for input values
if 'conversion_type' not in st.session_state:
    st.session_state.conversion_type = "Distance"
if 'value' not in st.session_state:
    st.session_state.value = 0.0
if 'from_unit' not in st.session_state:
    st.session_state.from_unit = "meters"
if 'to_unit' not in st.session_state:
    st.session_state.to_unit = "kilometers"


st.sidebar.header("Unit Converter Settings")


st.sidebar.subheader("Tips for Usage:")
st.sidebar.write("1. Select the type of conversion (Distance, Weight, Temperature, etc.).")
st.sidebar.write("2. Choose the units you want to convert between.")
st.sidebar.write("3. Enter the value and click 'Convert'.")

# Select Conversion Category
st.session_state.conversion_type = st.sidebar.selectbox(
    "Choose Conversion Type", 
    ["Distance", "Weight", "Temperature", "Frequency", "Area", "Data Transfer Rate", "Digital Storage", "Energy", "Fuel Economy", "Plane Angle", "Pressure", "Speed", "Time", "Volume"],
    index=["Distance", "Weight", "Temperature", "Frequency", "Area", "Data Transfer Rate", "Digital Storage", "Energy", "Fuel Economy", "Plane Angle", "Pressure", "Speed", "Time", "Volume"].index(st.session_state.conversion_type)
)

# Input Value
st.session_state.value = st.number_input("Enter the value to convert", min_value=0.0, step=0.1, value=st.session_state.value)

# Handle unit selection for each conversion type
if st.session_state.conversion_type == "Distance":
    units = ["meters", "kilometers", "centimeters", "millimeters", "nanometers", "miles", "yards", "feet", "inches", "nautical miles"]
elif st.session_state.conversion_type == "Weight":
    units = ["grams", "kilograms", "milligrams", "pounds", "ounces"]
elif st.session_state.conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
elif st.session_state.conversion_type == "Frequency":
    units = ["Hz", "kHz", "MHz", "GHz"]
elif st.session_state.conversion_type == "Area":
    units = ["square meters", "square kilometers", "square centimeters", "square millimeters", "square miles", "square yards", "square feet", "square inches"]
elif st.session_state.conversion_type == "Data Transfer Rate":
    units = ["bps", "kbps", "mbps", "gbps", "tbps"]
elif st.session_state.conversion_type == "Digital Storage":
    units = ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]
elif st.session_state.conversion_type == "Energy":
    units = ["joules", "kilojoules", "calories", "kilocalories", "watt-hours"]
elif st.session_state.conversion_type == "Fuel Economy":
    units = ["mpg (US)", "mpg (UK)", "L/100km", "km/L"]
elif st.session_state.conversion_type == "Plane Angle":
    units = ["radians", "degrees", "gradians"]
elif st.session_state.conversion_type == "Pressure":
    units = ["pascal", "kilopascal", "bar", "atm", "mmHg", "psi"]
elif st.session_state.conversion_type == "Speed":
    units = ["m/s", "km/h", "mph", "knots"]
elif st.session_state.conversion_type == "Time":
    units = ["seconds", "minutes", "hours", "days", "weeks", "months", "years"]
elif st.session_state.conversion_type == "Volume":
    units = ["liters", "milliliters", "cubic meters", "cubic centimeters", "cubic inches", "gallons (US)", "gallons (UK)", "quarts (US)", "quarts (UK)"]

# Select Units
st.session_state.from_unit = st.selectbox("From Unit", units, index=units.index(st.session_state.from_unit) if st.session_state.from_unit in units else 0)
st.session_state.to_unit = st.selectbox("To Unit", units, index=units.index(st.session_state.to_unit) if st.session_state.to_unit in units else 0)

# Button to perform the conversion
if st.button("Convert"):
    if st.session_state.value <= 0:
        st.error("Please enter a value greater than 0!")
    else:
        result = convert_units(st.session_state.value, st.session_state.from_unit, st.session_state.to_unit, st.session_state.conversion_type)
        st.success(f"Converted Value: {result} {st.session_state.to_unit}")
        st.write(f"Conversion Type: {st.session_state.conversion_type} | From: {st.session_state.from_unit} | To: {st.session_state.to_unit}")

# Reset Button
if st.button("Reset"):
    st.session_state.clear()

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("Created by ❤️ **Nimra Ulfat** 🌟✨", unsafe_allow_html=True)
