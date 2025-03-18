import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Boron Properties",
    page_icon="🧪",
    layout="wide"
)

# Shomate equation parameters for different phases of Boron (NIST WebBook)
shomate_params = {
    "solid": {"A": 10.18574, "B": 29.24415, "C": -18.02137, "D": 4.212326, "E": -0.550999},
    "liquid": {"A": 31.75003, "B": 2.556177e-7, "C": -6.456792e-8, "D": 5.616644e-9, "E": 2.705970e-7},
    "gas": {"A": 20.786, "B": 0.0, "C": 0.0, "D": 0.0, "E": 0.0}  # Approximate gas-phase values
}

# Function to calculate Cp from Shomate equation
def compute_Cp(phase, T):
    params = shomate_params[phase]
    t = T / 1000
    Cp = params["A"] + params["B"] * t + params["C"] * t**2 + params["D"] * t**3 + params["E"] / t**2
    return Cp

# Temperature ranges for different phases
T_solid = np.linspace(298, 1800, 500)
T_liquid = np.linspace(2350, 4137, 500)
T_gas = np.linspace(4200, 6000, 500)

Cp_solid = compute_Cp("solid", T_solid)
Cp_liquid = compute_Cp("liquid", T_liquid)
Cp_gas = compute_Cp("gas", T_gas)

# Radio button selection
a = st.radio(
    "Choose an element to explore:",
    [":red[B]  🔥 Boron", ":violet[K]  ✨ Potassium"],
    index=None
)

# Boron Section
if a == ":red[B]  🔥 Boron":
    st.markdown("# **Welcome to the World of Boron** 🧪")
    st.write("Explore the fascinating properties, occurrence, and uses of Boron.")

    st.header("📊 Heat Capacity (Cp) of Boron Across Phases")

    fig, ax = plt.subplots(figsize=(8, 5), facecolor="#0e1117")
    
    ax.plot(T_solid, Cp_solid, label="Solid (298 K - 1800 K)", color="blue")
    ax.plot(T_liquid, Cp_liquid, label="Liquid (2350 K - 4137 K)", color="red")
    ax.plot(T_gas, Cp_gas, label="Gas (4200 K - 6000 K)", color="green")

    ax.axvline(x=2350, color="gray", linestyle="--", label="Melting Point (2350 K)")
    ax.axvline(x=4200, color="gray", linestyle="--", label="Boiling Point (4200 K)")

    ax.set_facecolor("#0e1117")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("white")
    ax.spines["bottom"].set_color("white")

    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")
    ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.5)

    ax.set_title("Specific Heat Capacity of Boron", fontsize=14, fontweight="bold", color="white")
    ax.set_xlabel("Temperature (K)", fontsize=12, fontweight="bold")
    ax.set_ylabel("Cp (J/mol·K)", fontsize=12, fontweight="bold")
    ax.legend()

    st.pyplot(fig)

    st.markdown("📌 **Data Source:** [NIST WebBook](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7440428&Mask=2)")
