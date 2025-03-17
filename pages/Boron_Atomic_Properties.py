
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Boron - Atomic Properties",
    page_icon="🔬",
)

st.title("🔬 Boron - Atomic Properties")

col1, col2, col3 = st.columns(3)
col1.metric(label="Atomic Number", value="5")
col2.metric(label="Mass Number", value="10.81")
col3.write(" ")

col1, col2, col3 = st.columns(3)
col1.metric(label="Atomic Radius", value="87 pm")
col2.metric(label="Ionic Radius (B³⁺)", value="23 pm")
col3.metric(label="Density", value="2.34 g/cm³")

col1, col2, col3 = st.columns(3)
col1.metric(label="Oxidation States", value="+3")
col2.metric(label="Electronegativity", value="2.04")
col3.metric(label="Melting Point", value="2076°C")

col1, col2, col3 = st.columns(3)
col1.metric(label="Boiling Point", value="3927°C")
col2.metric(label="Vanderwaals Radius", value="192 pm")
col3.write(" ")

st.divider()

st.subheader("⚙️ Electronic Configuration")
st.latex("1s² 2s² 2p¹")

st.write("Boron has **three valence electrons** in the 2s and 2p orbitals, making it highly reactive in forming covalent bonds.")

st.divider()

st.subheader("⚡ Ionization Energy")
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

st.subheader("🌈 Atomic Spectra")
st.write("Boron’s atomic spectrum has strong lines in the UV and visible regions.")
st.image("https://physics.nist.gov/PhysRefData/ASD/lines_form.html", caption="Emission Spectrum of Boron", use_container_width=True)
