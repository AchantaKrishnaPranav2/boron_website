import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Boron - Isotopes",
    page_icon="🌟",
)

st.title("🌟 Boron - Isotopes")

st.write("Boron (5B) has **13 known isotopes**, ranging from atomic mass 7 to 21. However, only **¹⁰B and ¹¹B** occur naturally.")
st.write("¹⁰B makes up **19.9%** of natural boron, while **¹¹B** is the most abundant at **80.1%**.")

st.info("**Total isotopes of Boron** - **13**")
col1, col2 = st.columns(2)
col1.info("**Stable Isotopes** - **2**")
col2.info("**Radioactive Isotopes** - **11**")

st.divider()

st.header("🏆 Top 2 Isotopes of Boron (Abundance)")

top_isotopes = ["B-10", "B-11"]
abundances = [19.9, 80.1]
colors = ["#2a9d8f", "#fc8d62"]

df = pd.DataFrame({"Isotope": top_isotopes, "Abundance (%)": abundances})
fig = px.pie(df, names="Isotope", values="Abundance (%)", title="Distribution of Boron Isotopes",
             color=df["Isotope"], color_discrete_map={"B-10": "#2a9d8f", "B-11": "#fc8d62"}, hole=0.3)
fig.update_traces(textinfo='percent+label', textfont=dict(color='white'))
st.plotly_chart(fig, use_container_width=True)
