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
col3.metric(label="Melting Point", value="2076°C")

col1, col2, col3 = st.columns(3)
col1.metric(label="Boiling Point", value="3927°C")
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
fig.update_layout(plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", font_color="white",
                  title="Ionization Energies of Boron",
                  xaxis_title="Ionization Step",
                  yaxis_title="Energy (kJ/mol)")

st.plotly_chart(fig, use_container_width=True)  # FIXED: Added use_container_width=True
st.caption("Data Source: [WebElements Periodic Table](https://www.webelements.com/boron/atoms.html)")

st.divider()

# Allotropes
st.subheader("🔄 Allotropes")
st.write("""
Boron exists in several allotropes:
- **α-rhombohedral (α-R)**
- **β-rhombohedral (β-R)**: The most stable and common form.
- **β-tetragonal (β-T)**
- **γ-orthorhombic (γ)**

These allotropes are based on B₁₂ icosahedra structures. The β-rhombohedral phase is the most stable under ambient conditions, while others are metastable but can exist at room temperature due to negligible transformation rates.
""")
st.caption("Information Source: [Wikipedia - Boron](https://en.wikipedia.org/wiki/Boron)")

st.divider()

# Atomic Spectra
st.subheader("🌈 Atomic Spectra")
st.write("""
Boron’s atomic spectrum features strong lines in the ultraviolet (UV) and visible regions. Notable emission lines include:
- **B II** at **345.10 nm**
- **B I** at **249.77 nm**

These spectral lines are crucial in various applications, including spectroscopy and materials science.
""")
st.caption("Data Source: [NIST Physical Measurement Laboratory](https://physics.nist.gov/PhysRefData/Handbook/Tables/borontable2.htm)")

# Displaying Emission Spectrum Image
st.image("https://www.nist.gov/sites/default/files/styles/960_x_960_limit/public/images/2020/04/20/boron_spectrum.png", 
         caption="Emission Spectrum of Boron", use_column_width=True)  # FIXED: Added use_container_width=True

st.divider()

# Electron Affinity
st.subheader("🧲 Electron Affinity")
st.write("""
Boron has an electron affinity of approximately **26.7 kJ/mol**. This property indicates the energy change when an electron is added to a neutral boron atom, forming a negative ion.
""")
st.caption("Data Source: [WebElements Periodic Table](https://www.webelements.com/boron/atoms.html)")


