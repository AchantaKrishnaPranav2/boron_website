import streamlit as st
import plotly.express as px
import pandas as pd

# Set Streamlit page config
st.set_page_config(page_title="Boron - Atomic Properties", page_icon="🔬")
a = st.radio(
    "Choose an element to explore:",
    [":red[B]  🔥 Boron", ":violet[K]  ✨ Potassium"],
    index=None)
if a == ":red[B]  🔥 Boron":
    st.title("🔬 Boron - Atomic Properties")
    st.image("https://media3.giphy.com/media/Kg1ttGFEuMc9QvuYVa/giphy.gif")
    
    
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
