import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Boron - Isotopes",
    page_icon="🌟",
)

st.title("🌟 Boron - Isotopes")

# Introduction
st.write("""
Boron (**5B**) has **13 known isotopes**, ranging from atomic mass **7 to 21**.  
However, only **¹⁰B and ¹¹B** occur naturally.  

- **¹⁰B**: Accounts for **19.9%** of natural boron.  
- **¹¹B**: The most abundant isotope at **80.1%**.  
- The remaining **11 isotopes** are **radioactive** with short half-lives.  
""")

st.info("**Total Isotopes of Boron**: **13 (2 Stable, 11 Radioactive)**")

# Stable & Radioactive Isotope Summary
col1, col2 = st.columns(2)
col1.success("✅ **Stable Isotopes**: **2** (¹⁰B, ¹¹B)")
col2.warning("⚠ **Radioactive Isotopes**: **11** (Short-lived)")

st.divider()

# 🏆 Stable Isotopes Chart
st.header("🏆 Stable Boron Isotopes (Abundance)")

top_isotopes = ["¹⁰B", "¹¹B"]
abundances = [19.9, 80.1]

df = pd.DataFrame({"Isotope": top_isotopes, "Abundance (%)": abundances})
fig = px.pie(df, names="Isotope", values="Abundance (%)",
             title="Distribution of Boron Isotopes",
             color=df["Isotope"], color_discrete_map={"¹⁰B": "#2a9d8f", "¹¹B": "#fc8d62"}, hole=0.3)

fig.update_traces(textinfo='percent+label', textfont=dict(color='white'), hoverinfo="label+percent")
st.plotly_chart(fig, use_container_width=True)

st.caption("Data Source: [Royal Society of Chemistry](https://periodic-table.rsc.org/element/5/boron)")

st.divider()

# ⚛️ Radioactive Isotopes Table
st.subheader("⚛️ Radioactive Isotopes of Boron")

st.write("""
These isotopes **decay rapidly**, making them unsuitable for most applications.
However, their properties help in **nuclear physics research**.
""")

radioactive_isotopes = {
    "Isotope": ["⁷B", "⁸B", "⁹B", "¹²B", "¹³B", "¹⁴B", "¹⁵B", "¹⁶B", "¹⁷B", "¹⁸B", "¹⁹B"],
    "Half-life": ["<10⁻²² s", "770 ms", "8.3 ms", "20.2 ms", "17.33 ms", "12.5 ms", "9.8 ms", "0.92 ms", "5.08 ms", "26.9 ms", "2.92 ms"],
    "Decay Mode": ["p-emission", "β⁺ decay", "β⁺ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay", "β⁻ decay"]
}

df_radioactive = pd.DataFrame(radioactive_isotopes)
st.dataframe(df_radioactive.style.set_properties(**{'background-color': 'black', 'color': 'white'}), use_container_width=True)

st.caption("Data Source: [NIST WebBook](https://webbook.nist.gov/cgi/inchi?ID=C7440428&Mask=20#Ion-Energetics)")

st.divider()

# 🔬 Applications of Boron Isotopes
st.subheader("🔬 Applications of Boron Isotopes")

st.write("""
- **¹⁰B (Boron-10)**  
  - Used in **nuclear reactors** as a neutron absorber.  
  - Plays a crucial role in **boron neutron capture therapy (BNCT)**, a cancer treatment.  
- **¹¹B (Boron-11)**  
  - Preferred in **Nuclear Magnetic Resonance (NMR) Spectroscopy** due to its spin properties.  
  - Utilized in **semiconductor industries** for doping silicon.  
""")

st.caption("Information Source: [Wikipedia - Boron Isotopes](https://en.wikipedia.org/wiki/Isotopes_of_boron)")
