import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Boron - Isotopes",
    page_icon="🌟",
)
a = st.radio(
    "Choose an element to explore:",
    [":red[B]  🔥 Boron", ":violet[K]  ✨ Potassium"],
    index=None)
if a == ":red[B]  🔥 Boron":
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
elif a == ":violet[K]  ✨ Potassium":
    st.title("🌟 Potassium - Isotopes")

    st.write("Potassium (19K) has 26 known isotopes, ranging from atomic mass 32 to 57. However, only three of these occur naturally: **³⁹K, ⁴⁰K, and ⁴¹K**. Among them, **³⁹K** and **⁴¹K** are stable, while **⁴⁰K** is radioactive, undergoing beta decay with a half-life of 1.248 billion years.")
    st.write("⁴⁰K is especially significant because it contributes to Earth's natural radioactivity. It undergoes beta decay, forming calcium-40 and argon-40, making it useful in potassium-argon dating to determine the age of rocks and minerals.")
    st.info("**Total isotopes of potassium** - **26**")
    col1, col2 = st.columns(2)
    col1.info("**Stable** - **2**")
    col2.info("**Radioactive** - **24**")
    
    st.divider()
    
    st.header("🏆 Top 3 Isotopes of Potassium (Abundance)")
    col1, col2 = st.columns([0.5, 1])
    col1.info("**Only 2 isotopes are stable**")
    col1.markdown("""
        <div style="background-color: #2a9d8f; color: white; font-weight: bold; padding: 10px; border-radius: 10px;">
            Potassium 39 - 93.3%
        </div>
        """, unsafe_allow_html=True)
    
    col1.markdown("""
        <div style="background-color: #fc8d62; color: white; font-weight: bold; padding: 10px; border-radius: 10px;">
            Potassium 41 - 6.7%
        </div>
        """, unsafe_allow_html=True)
    
    col1.markdown("""
        <div style="background-color: #8da0cb; color: white; font-weight: bold; padding: 10px; border-radius: 10px;">
            Potassium 40 - 0.0117%
        </div>
        """, unsafe_allow_html=True)
    
    # Pie Chart with matching colors
    top_isotopes = ["K-39", "K-41", "K-40"]
    abundances = [93.3, 6.7, 0.0117]
    colors = ["#2a9d8f", "#fc8d62", "#8da0cb"]
    
    df = pd.DataFrame({"Isotope": top_isotopes, "Abundance (%)": abundances})
    fig = px.pie(df, names="Isotope", values="Abundance (%)", title="Distribution of Potassium Isotopes",
                 color=df["Isotope"], color_discrete_map={"K-39": "#2a9d8f", "K-41": "#fc8d62", "K-40": "#8da0cb"}, hole=0.3)
    fig.update_traces(textinfo='percent+label', textfont=dict(color='white'))
    col2.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    st.header("🔋 Decay Simulation")
    st.markdown("The isotope decay formula follows exponential decay and is given by:")
    st.latex("N = N_0e^{-\\lambda t}")
    st.latex("\\lambda = \\ln2 / t_{1/2}")
    st.write("        ")
    col1, col2 = st.columns(2)
    col1.markdown("$\\lambda = $ Decay constant")
    col1.markdown("$t_{1/2} = $ Half-life")
    col1.markdown("$N = $ Number of atoms remaining after time")
    col2.markdown("$N_0 = $ Initial number of atoms")
    col2.markdown("$t = $ Time elapsed")
    
    potassium_isotopes = {
        "K-40": {"half_life": 1.248e9, "unit": "years"},
        "K-42": {"half_life": 12.36, "unit": "hours"},
        "K-43": {"half_life": 22.3, "unit": "hours"},
        "K-44": {"half_life": 22.1, "unit": "minutes"},
        "K-45": {"half_life": 17.8, "unit": "minutes"},
    }
    
    selected_isotope = st.selectbox("Select a Potassium Isotope:", list(potassium_isotopes.keys()))
    
    half_life = potassium_isotopes[selected_isotope]["half_life"]
    unit = potassium_isotopes[selected_isotope]["unit"]
    
    if selected_isotope:
        st.info(f"The half-life of {selected_isotope} is {half_life} {unit}")
    
    unit_conversion = {"seconds": 1, "minutes": 60, "hours": 3600, "years": 365 * 24 * 3600}
    half_life_seconds = half_life * unit_conversion[unit]
    
    initial_atoms = st.slider("Initial number of atoms (N₀):", 1, 1000, 500)
    
    if unit == "seconds":
        max_time = 10 * half_life
    elif unit == "minutes":
        max_time = 10 * half_life
    elif unit == "hours":
        max_time = 5 * half_life
    else:
        max_time = 3 * half_life
    
    elapsed_time = st.slider(f"Select elapsed time ({unit}):", 0.0, max_time, 0.1)
    
    decay_constant = np.log(2) / half_life_seconds
    N_remaining = initial_atoms * np.exp(-decay_constant * (elapsed_time * unit_conversion[unit]))
    st.info(f"After **{elapsed_time:.2f} {unit}**, approximately **{N_remaining:.2f}** atoms remain.")
    
    time_values = np.linspace(0, max_time, 500)
    N_values = initial_atoms * np.exp(-decay_constant * (time_values * unit_conversion[unit]))
    
    plt.style.use("seaborn-v0_8-dark")
    fig, ax = plt.subplots(figsize=(7, 4), facecolor="#0e1117")
    ax.plot(time_values, N_values, label=f"{selected_isotope} Decay", color="#5cde1f", linewidth=2, marker="o", markersize=4, markerfacecolor="white", markeredgecolor="#5cde1f", alpha=0.8)
    
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
    ax.set_title(f"Exponential Decay of {selected_isotope}", fontsize=14, fontweight="bold", color="white")
    ax.set_xlabel(f"Time ({unit})", fontsize=12, fontweight="bold")
    ax.set_ylabel("Number of Atoms", fontsize=12, fontweight="bold")
    st.pyplot(fig)
