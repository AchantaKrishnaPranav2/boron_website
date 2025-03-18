import streamlit as st
import plotly.express as px
import pandas as pd

# Set Streamlit page config
st.set_page_config(page_title="Boron - Atomic Properties", page_icon="🔬")

st.title("🔬 Boron - Atomic Properties")

# ----------------------------------------
# 🔹 Basic Atomic Properties
# ----------------------------------------
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

# ----------------------------------------
# ⚙️ Electronic Configuration
# ----------------------------------------
st.subheader("⚙️ Electronic Configuration")
st.latex(r"1s^2\ 2s^2\ 2p^1")
st.write("Boron has **three valence electrons** in the 2s and 2p orbitals, making it versatile in forming covalent bonds.")

st.divider()

# ----------------------------------------
# ⚡ Ionization Energies
# ----------------------------------------
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

st.plotly_chart(fig, use_container_width=True)
st.caption("Data Source: [WebElements Periodic Table](https://www.webelements.com/boron/atoms.html)")

st.divider()

# ----------------------------------------
# 🔄 Allotropes
# ----------------------------------------
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

# ----------------------------------------
# 🌈 Atomic Spectra
# ----------------------------------------
st.subheader("🌈 Atomic Spectra")
st.write("""
Boron’s atomic spectrum features strong lines in the ultraviolet (UV) and visible regions. Notable emission lines include:
- **B II** at **345.10 nm**
- **B I** at **249.77 nm**

These spectral lines are crucial in various applications, including spectroscopy and materials science.
""")
st.caption("Data Source: [NIST Physical Measurement Laboratory](https://physics.nist.gov/PhysRefData/Handbook/Tables/borontable2.htm)")

# ✅ **1️⃣ Interactive Emission Spectrum using Plotly**
st.subheader("🔬 Interactive Emission Spectrum")

# Emission spectrum data
spectra_data = {
    "Wavelength (nm)": [249.77, 345.10, 412.12, 455.35, 520.56],  
    "Intensity": [100, 80, 60, 50, 40]  
}

df_spectra = pd.DataFrame(spectra_data)

fig = px.bar(df_spectra, x="Wavelength (nm)", y="Intensity", 
             text="Wavelength (nm)", color="Intensity",
             color_continuous_scale="plasma")

fig.update_traces(textfont_size=12, textposition="outside")

fig.update_layout(title="Boron Emission Spectrum",
                  xaxis_title="Wavelength (nm)",
                  yaxis_title="Relative Intensity",
                  plot_bgcolor="black",
                  paper_bgcolor="black",
                  font_color="white")

st.plotly_chart(fig, use_container_width=True)

# ✅ **2️⃣ Simulated Spectral Gradient using CSS & HTML**
st.subheader("🌈 Simulated Boron Emission Spectrum")

html_code = """
<style>
.spectrum-bar {
    width: 100%;
    height: 50px;
    background: linear-gradient(to right, 
        black 0%, violet 10%, blue 20%, cyan 30%, 
        green 40%, yellow 50%, orange 60%, red 70%, black 100%);
    border-radius: 5px;
}
</style>
<div class="spectrum-bar"></div>
"""

st.markdown(html_code, unsafe_allow_html=True)

# ✅ **3️⃣ Emission Spectrum Table**
st.subheader("📊 Emission Line Data for Boron")

df_table = pd.DataFrame({
    "Wavelength (nm)": [249.77, 345.10, 412.12, 455.35, 520.56],
    "Emission Type": ["B I", "B II", "B III", "B IV", "B V"],
    "Relative Intensity": ["Strong", "Medium", "Weak", "Weak", "Very Weak"]
})

st.dataframe(df_table, use_container_width=True)


st.divider()

# ----------------------------------------
# 🧲 Electron Affinity
# ----------------------------------------
st.subheader("🧲 Electron Affinity")
st.write("""
Boron has an electron affinity of approximately **26.7 kJ/mol**. This property indicates the energy change when an electron is added to a neutral boron atom, forming a negative ion.
""")
st.caption("Data Source: [WebElements Periodic Table](https://www.webelements.com/boron/atoms.html)")

# 📚 Information Sources
st.caption("🔗 Additional Data Source: [NIST Physical Measurement Laboratory](https://physics.nist.gov/PhysRefData/Handbook/Tables/borontable2.htm)")


