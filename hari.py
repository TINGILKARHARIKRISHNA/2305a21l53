import streamlit as st

# Function to calculate Efficiency and Copper Losses
def Gen_Eff(V, CL, IL, K, Rsh, Ra):
    try:
        # Calculations
        Ish = V / Rsh
        Ia = K * IL - Ish
        CUL = (Ish**2) * Rsh + (Ia**2) * Ra
        Eff = ((K * V * IL - CL - CUL) / (K * V * IL)) * 100
        return Eff, CUL
    except ZeroDivisionError:
        return "Error: Division by zero", None

# Streamlit App
st.title("2305A21L53-PS12")
st.text("DC Shunt Motor Efficiency Calculator")

st.markdown("""
This app calculates the **efficiency** and **copper losses** of a DC shunt motor based on the provided inputs.
""")

# Input fields
V = st.number_input("Voltage (V)", min_value=0.0, step=0.1, format="%.2f")
CL = st.number_input("Core Losses (CL) in watts", min_value=0.0, step=0.1, format="%.2f")
IL = st.number_input("Full Load Current (IL) in Amps", min_value=0.0, step=0.1, format="%.2f")
K = st.number_input("Loading on Generator (K)", min_value=0.0, step=0.1, format="%.2f")
Rsh = st.number_input("Shunt Field Resistance (Rsh) in Ohms", min_value=0.0, step=0.1, format="%.2f")
Ra = st.number_input("Armature Resistance (Ra) in Ohms", min_value=0.0, step=0.1, format="%.2f")

# Calculate button
if st.button("Calculate Efficiency"):
    Eff, CUL = Gen_Eff(V, CL, IL, K, Rsh, Ra)
    if Eff != "Error: Division by zero":
        st.success(f"Efficiency: {Eff:.2f}%")
        st.info(f"Copper Losses: {CUL:.2f} W")
    else:
        st.error("Error: Division by zero. Please check your inputs.")

# Footer
st.markdown("""
**Note:** Ensure that all inputs are non-zero and valid for accurate calculations.
""")
