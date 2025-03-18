import streamlit as st
import plotly.express as px
import pandas as pd

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
    "Ionization Step": ["1st", "2nd", "3rd"],
    "Energy (kJ/mol)": [800.6, 2427, 3659]
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
st.image("https://physics.nist.gov/PhysRefData/ASD/lines_form.html", caption="Emission Spectrum of Boron", use_container_width=True)

st.divider()

# Electron Affinity
st.subheader("🧲 Electron Affinity")
st.write("""
Boron has an electron affinity of approximately **0.27974 eV**. This property indicates the energy change when an electron is added to a neutral boron atom, forming a negative ion. [Source: NIST](https://webbook.nist.gov/cgi/inchi?ID=C7440428&Mask=20#Ion-Energetics)
""")

