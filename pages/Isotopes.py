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
    [":red[B]  🔥 Boron", ":violet[K]  ✨ Potassium",  ":orange[Kr] 🍀 Krypton"],
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
    import numpy as np
    import matplotlib.pyplot as plt
    import streamlit as st
    
    # Header
    st.header("🔋 Decay Simulation")
    st.markdown("The isotope decay formula follows exponential decay and is given by:")
    st.latex("N = N_0e^{-\\lambda t}")
    st.latex("\\lambda = \\ln2 / t_{1/2}")
    st.write("        ")
    
    # Columns for equation terms
    col1, col2 = st.columns(2)
    col1.markdown("$\\lambda = $ Decay constant")
    col1.markdown("$t_{1/2} = $ Half-life")
    col1.markdown("$N = $ Number of atoms remaining after time")
    col2.markdown("$N_0 = $ Initial number of atoms")
    col2.markdown("$t = $ Time elapsed")
    
    # Dictionary of Boron Isotopes and their half-lives
    boron_isotopes = {
        "B-8": {"half_life": 0.770, "unit": "seconds"},
        "B-10": {"half_life": 1e20, "unit": "years"},  # Stable isotope
        "B-11": {"half_life": 1e20, "unit": "years"},  # Stable isotope
        "B-12": {"half_life": 20.2, "unit": "milliseconds"},
    }
    
    # Select Boron Isotope
    selected_isotope = st.selectbox("Select a Boron Isotope:", list(boron_isotopes.keys()))
    
    half_life = boron_isotopes[selected_isotope]["half_life"]
    unit = boron_isotopes[selected_isotope]["unit"]
    
    if selected_isotope:
        st.info(f"The half-life of {selected_isotope} is {half_life} {unit}")
    
    # Convert half-life to seconds
    unit_conversion = {"seconds": 1, "milliseconds": 1e-3, "years": 365 * 24 * 3600}
    half_life_seconds = half_life * unit_conversion[unit]
    
    # Initial Atoms Slider
    initial_atoms = st.slider("Initial number of atoms (N₀):", 1, 1000, 500)
    
    # Adjust max time for simulation
    if unit == "seconds":
        max_time = 10 * half_life
    elif unit == "milliseconds":
        max_time = 10 * half_life
    elif unit == "years":
        max_time = 3 * half_life
    
    elapsed_time = st.slider(f"Select elapsed time ({unit}):", 0.0, max_time, 0.1)
    
    # Decay calculations
    if selected_isotope in ["B-10", "B-11"]:
        N_remaining = initial_atoms  # Stable isotopes
        st.info(f"{selected_isotope} is a **stable isotope**, meaning it does not decay.")
    else:
        decay_constant = np.log(2) / half_life_seconds
        N_remaining = initial_atoms * np.exp(-decay_constant * (elapsed_time * unit_conversion[unit]))
        st.info(f"After **{elapsed_time:.2f} {unit}**, approximately **{N_remaining:.2f}** atoms remain.")
    
    # Generate decay curve
    if selected_isotope not in ["B-10", "B-11"]:  # Skip plotting for stable isotopes
        time_values = np.linspace(0, max_time, 500)
        N_values = initial_atoms * np.exp(-decay_constant * (time_values * unit_conversion[unit]))
    
        plt.style.use("seaborn-v0_8-dark")
        fig, ax = plt.subplots(figsize=(7, 4), facecolor="#0e1117")
        ax.plot(time_values, N_values, label=f"{selected_isotope} Decay", color="#ff5733", linewidth=2, marker="o", markersize=4, markerfacecolor="white", markeredgecolor="#ff5733", alpha=0.8)
    
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

elif a == ":orange[Kr] 🍀 Krypton" :
    st.title("☢️ Krypton - Isotpes")

    st.write("Krypton (36Kr) has 34 known isotopes, with atomic mass numbers ranging from 67 to 103. Among these, naturally occurring krypton consists of five stable isotopes along with one isotope, ⁷⁸Kr, which is considered quasi-stable due to its extremely long half-life of 9.2 × 10²¹ years. This half-life is so vast that, for practical purposes, ⁷⁸Kr is often regarded as stable.")
    st.write("Additionally, krypton in Earth's atmosphere contains minute traces of radioactive isotopes that are continuously formed through interactions between cosmic rays and atmospheric krypton. One such isotope is ⁸¹Kr, a cosmogenic nuclide with a half-life of 230,000 years, making it useful for dating ancient groundwater and ice cores. Another important isotope is ⁸⁵Kr, a radioactive noble gas with a half-life of 10.76 years, primarily produced as a byproduct of nuclear fission in reactors and during nuclear weapons testing.")
    st.info("**Total isotopes of krypton** - **34**")
    col1, col2 = st.columns(2)
    col1.info("**Stable** - **5**")
    col2.info("**Radioactive** - **25**")
    
    st.divider()
    
    st.header("🎖️ Top 5 Isotopes of Krypton (Abundance)")
    st.write("      ")
    st.write("      ")
    col1, col2 = st.columns([0.5, 1])
    col1.info("**All these 5 isotopes are stable**")
    col1.markdown("""
        <div style="
            background-color: #2a9d8f; 
            color: white    ; 
            font-weight: bold;
            padding: 10px; 
            border-radius: 10px;">
            Krypton 84 - 57%
        </div>
        """, unsafe_allow_html=True)
    
    col1.markdown("""
        <div style="
            background-color: #fc8d62; 
            color: white; 
            font-weight: bold;
            padding: 10px; 
            border-radius: 10px;">
            Krypton 86 - 17.3%
        </div>
        """, unsafe_allow_html=True)
    col1.markdown("""
        <div style="
            background-color: #8da0cb; 
            color: white; 
            font-weight: bold;
            padding: 10px; 
            border-radius: 10px;">
            Krypton 82 - 11.6%
        </div>
        """, unsafe_allow_html=True)
    col1.markdown("""
        <div style="
            background-color: #e78ac3; 
            color: white; 
            font-weight: bold;
            padding: 10px; 
            border-radius: 10px;">
            Krypton 83 - 11.5%
        </div>
        """, unsafe_allow_html=True)
    col1.markdown("""
        <div style="
            background-color: #a6d854; 
            color: white; 
            font-weight: bold;
            padding: 10px; 
            border-radius: 10px;">
            Krypton 80 - 2.29%
        </div>
        """, unsafe_allow_html=True)
    col1.markdown("""
        <div style="
            background-color: #ffd92f; 
            color: white; 
            font-weight: bold;
            padding: 10px; 
            border-radius: 10px;">
            others - 0.38%
        </div>
        """, unsafe_allow_html=True)
    
    
    isotopes = ["Kr-84", "Kr-86", "Kr-82", "Kr-83", "Kr-80", "Others"]
    percentages = [56.98, 17.28, 11.58, 11.49, 2.29, 0.38]  
    df = pd.DataFrame({"Isotope": isotopes, "Abundance (%)": percentages})
    fig = px.pie(df, names = "Isotope", values = "Abundance (%)", title="Distribution of Krypton Isotopes",
                 color_discrete_sequence=px.colors.qualitative.Set2, hole=0.3)
    fig.update_traces(textinfo='percent+label', textfont=dict(color='white'))
    col2.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    st.header("📉 Decay Simulation")
    
    st.markdown("The isotope decay formula follows exponential decay and is given by:")
    st.latex("N = N_0e^{-\lambda t}")
    st.latex("\lambda = \ln2 / t_{1/2}")
    st.write("        ")
    col1, col2 = st.columns(2)
    col1.markdown("$\lambda = $ Decay constant")
    col1.markdown("$t_{1/2} = $ Half-life")
    col1.markdown("$N = $ Number of atoms remaining after time")
    col2.markdown("$N_0 = $ Initial number of atoms")
    col2.markdown("$t = $ Time elapsed")
    
    krypton_isotopes = {
        "Kr-79": {"half_life": 35.0, "unit": "hours"},
        "Kr-78": {"half_life": 9.2e21, "unit": "years"},
        "Kr-81": {"half_life": 229000.0, "unit": "years"},
        "Kr-85": {"half_life": 10.76, "unit": "years"},
        "Kr-85m": {"half_life": 4.48, "unit": "hours"},
        "Kr-87": {"half_life": 76.3, "unit": "minutes"},
        "Kr-88": {"half_life": 2.84, "unit": "hours"},
        "Kr-89": {"half_life": 3.15, "unit": "minutes"},
        "Kr-90": {"half_life": 32.3, "unit": "seconds"},
        "Kr-91": {"half_life": 8.6, "unit": "seconds"},
        "Kr-92": {"half_life": 1.84, "unit": "seconds"},
    }
    
    selected_isotope = st.selectbox("Select a Krypton Isotope:", list(krypton_isotopes.keys()))
    
    # Get the selected isotope's half-life and unit
    half_life = krypton_isotopes[selected_isotope]["half_life"]
    unit = krypton_isotopes[selected_isotope]["unit"]
    
    if selected_isotope:
        st.info(f"The half life of {selected_isotope} is  {half_life} {unit}")
    
    # Convert half-life to seconds for calculation
    unit_conversion = {"seconds": 1, "minutes": 60, "hours": 3600, "years": 365 * 24 * 3600}
    half_life_seconds = half_life * unit_conversion[unit]
    
    # Initial number of atoms
    initial_atoms = st.slider("Initial number of atoms (N₀):", 1, 1000, 500)
    
    # Adjust time scale for the simulation
    if unit == "seconds":
        max_time = 10 * half_life
    elif unit == "minutes":
        max_time = 10 * half_life
    elif unit == "hours":
        max_time = 5 * half_life
    else:  # years
        max_time = 3 * half_life
    
    # Slider for elapsed time
    elapsed_time = st.slider(f"Select elapsed time ({unit}):", 0.0, max_time, 0.1)
    
    # Compute decay constant
    decay_constant = np.log(2) / half_life_seconds
    
    # Compute remaining atoms
    N_remaining = initial_atoms * np.exp(-decay_constant * (elapsed_time * unit_conversion[unit]))
    
    # Display remaining atoms
    st.info(f"After **{elapsed_time:.2f} {unit}**, approximately **{N_remaining:.2f}** atoms remain.")
    
    # Generate decay curve
    time_values = np.linspace(0, max_time, 500)
    N_values = initial_atoms * np.exp(-decay_constant * (time_values * unit_conversion[unit]))
    
    # Plot
    plt.style.use("seaborn-v0_8-dark")
    fig, ax = plt.subplots(figsize=(7, 4), facecolor="#0e1117")
    ax.plot(time_values, N_values, label=f"{selected_isotope} Decay", color="#5cde1f", linewidth=2, marker="o", markersize=4, markerfacecolor="white", markeredgecolor="#5cde1f", alpha=0.8)
    
    ax.set_facecolor("#0e1117")  # Dark background
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("white")
    ax.spines["bottom"].set_color("white")
    
    ax.xaxis.label.set_color("white")  # X label color
    ax.yaxis.label.set_color("white")  # Y label color
    ax.tick_params(axis="x", colors="white")  # X ticks color
    ax.tick_params(axis="y", colors="white")  # Y ticks color
    
    ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.5)
    
    ax.set_title(f"Exponential Decay of {selected_isotope}", fontsize=14, fontweight="bold", color="white")
    ax.set_xlabel(f"Time ({unit})", fontsize=12, fontweight="bold")
    ax.set_ylabel("Number of Atoms", fontsize=12, fontweight="bold")
    st.pyplot(fig)
    
    st.divider()
