import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Boron - Atomic Properties",
    page_icon="🔬",
)

st.title("🔬 Boron - Atomic Properties")

# Displaying basic atomic properties
col1, col2, col3 = st.columns(3)
col1.metric(label="Atomic Number", value="5")
col2.metric(label="Relative Atomic Mass", value="10.81")
col3.write(" ")

col1, col2, col3 = st.columns(3)
col1.metric(label="Atomic Radius", value="87 pm")
col2.metric(label="Density", value="2.34 g/cm³")
col3.metric(label="Melting Point", value="2077°C")

col1, col2, col3 = st.columns(3)
col1.metric(label="Boiling Point", value="4000°C")
col2.metric(label="Electronegativity", value="2.04")
col3.write(" ")

st.divider()

# Electronic Configuration
st.subheader("⚙️ Electronic Configuration")
st.latex(r"1s^2\ 2s^2\ 2p^1")
st.write("Boron has **three valence electrons** in the 2s and 2p orbitals, making it versatile in forming covalent bonds.")

st.divider()

# Ionization Energies
st.subheader("⚡ Ionization Energies")
ionization_data = {
    "Ionization Step": ["1st", "2nd", "3rd", "4th", "5th"],
    "Energy (kJ/mol)": [800.6, 2427.1, 3659.7, 25025.8, 32826.7]
}

df_ionization = pd.DataFrame(ionization_data)
fig = px.bar(df_ionization, x="Ionization Step", y="Energy (kJ/mol)",
             text="Energy (kJ/mol)", color="Energy (kJ/mol)",
             color_continuous_scale="viridis", height=400)

fig.update_traces(textfont_size=12, textposition="outside")
fig.update_layout(plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", font_color="white")

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Allotropes
st.subheader("🔄 Allotropes")
st.write("""
Boron exists in several allotropes:
- **α-rhombohedral (α-R)**
- **β-rhombohedral (β-R)**: The most stable and common form.
- **β-tetragonal (β-T)**
- **γ-orthorhombic (γ)**

These allotropes are based on B₁₂ icosahedra structures. The β-rhombohedral phase is the most stable under ambient conditions, while others are metastable but can exist at room temperature due to negligible transformation rates. [Source: Wikipedia](https://en.wikipedia.org/wiki/Boron)
""")

st.divider()

# Atomic Spectra
st.subheader("🌈 Atomic Spectra")
st.write("""
Boron’s atomic spectrum features strong lines in the ultraviolet (UV) and visible regions. These spectral lines are crucial in various applications, including spectroscopy and materials science.
""")
st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Boron_spectrum_visible.png", caption="Emission Spectrum of Boron", use_container_width=True)

st.divider()

# Electron Affinity
st.subheader("🧲 Electron Affinity")
st.write("""
Boron has an electron affinity of approximately **26.7 kJ/mol**. This property indicates the energy change when an electron is added to a neutral boron atom, forming a negative ion. [Source: WebElements](https://www.webelements.com/boron/atoms.html)
""")

st.divider()

# Additional Graph: Atomic Radius vs. Ionization Energy
st.subheader("📊 Atomic Radius vs. Ionization Energy")
atomic_data = {
    "Element": ["Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine"],
    "Atomic Radius (pm)": [87, 77, 75, 73, 71],
    "1st Ionization Energy (kJ/mol)": [800.6, 1086.5, 1402.3, 1313.9, 1681]
}

df_atomic = pd.DataFrame(atomic_data)
fig2 = px.scatter(df_atomic, x="Atomic Radius (pm)", y="1st Ionization Energy (kJ/mol)",
                  text="Element", size="1st Ionization Energy (kJ/mol)", color="Element",
                  hover_name="Element", height=400)

fig2.update_traces(textposition="top center")
fig2.update_layout(plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", font_color="white")

st.plotly_chart(fig2, use_container_width=True)

