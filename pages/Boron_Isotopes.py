import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Boron - Isotopes",
    page_icon="🌟",
)

st.title("🌟 Boron - Isotopes")

# Introduction
st.write("Boron (**5B**) has **13 known isotopes**, ranging from atomic mass **7 to 21**. However, only **¹⁰B and ¹¹B** occur naturally.")
st.write("¹⁰B constitutes **19.9%** of natural boron, while **¹¹B** is the most abundant at **80.1%**.")

st.info("**Total Isotopes of Boron** - **13**")

# Stable & Radioactive Isotope Summary
col1, col2 = st.columns(2)
col1.success("**Stable Isotopes** - **2**")
col2.warning("**Radioactive Isotopes** - **11**")

st.divider()

# Stable Isotopes Chart
st.header("🏆 Top 2 Isotopes of Boron (Abundance)")

top_isotopes = ["¹⁰B", "¹¹B"]
abundances = [19.9, 80.1]

df = pd.DataFrame({"Isotope": top_isotopes, "Abundance (%)": abundances})
fig = px.pie(df, names="Isotope", values="Abundance (%)",
             title="Distribution of Boron Isotopes",
             color=df["Isotope"], color_discrete_map={"¹⁰B": "#2a9d8f", "¹¹B": "#fc8d62"}, hole=0.3)

fig.update_traces(textinfo='percent+label', textfont=dict(color='white'))
st.plotly_chart(fig, use_container_width=True)

st.caption("Data Source: [Periodic Table - Royal Society of Chemistry](https://periodic-table.rsc.org/element/5/boron)")

st.divider()

# Radioactive Isotopes Table
st.subheader("⚛️ Radioactive Isotopes of Boron")

radioactive_isotopes = {
    "Isotope": ["⁷B", "⁸B", "⁹B", "¹²B", "¹³B", "¹⁴B", "¹⁵B", "¹⁶B", "¹⁷B", "¹⁸B", "¹⁹B"],
    "Half-life": ["<10⁻²⁲ s", "770 ms", "8.3 ms", "20.2 ms", "17.33 ms", "12.5 ms", "9.8 ms", "0.92 ms", "5.08 ms", "26.9 ms", "2.92 ms"],
    "Decay Mode": ["p-emission", "β⁺ decay", "β⁺ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay"]
}

df_radioactive = pd.DataFrame(radioactive_isotopes)
st.dataframe(df_radioactive, use_container_width=True)

st.caption("Data Source: [NIST WebBook - Boron](https://webbook.nist.gov/cgi/inchi?ID=C7440428&Mask=20#Ion-Energetics)")

st.divider()

# Additional Information
st.subheader("🔬 Isotope Applications")
st.write("""
- **¹⁰B** is widely used in **nuclear reactors** and **radiation therapy** due to its high neutron absorption.
- **¹¹B** is preferred in **NMR spectroscopy** because of its nuclear spin properties.
""")
st.caption("Information Source: [Wikipedia - Boron Isotopes](https://en.wikipedia.org/wiki/Isotopes_of_boron)")

