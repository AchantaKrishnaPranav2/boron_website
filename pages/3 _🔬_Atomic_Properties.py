import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Atomic Properties", page_icon="🔬")
a = st.radio(
    "Choose an element to explore:",
    [":red[B]  🔥 Boron", ":violet[K]  ✨ Potassium",  ":orange[Kr] 🍀 Krypton"],
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
    col3.metric(label="Crystal Structure", value="Icosahedral")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Atomic Radius", value="87 pm")
    col2.metric(label="Ionic Radius (B³⁺)", value="27 pm")
    col3.metric(label="Density", value="2.34 g/cm³")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Melting Point", value="2076°C")
    col2.metric(label="Boiling Point", value="3927°C")
    col3.metric(label="Electronegativity", value="2.04")

    st.divider()

    # ----------------------------------------
    # ⚙️ Electronic Configuration
    # ----------------------------------------
    st.subheader("⚙️ Electronic Configuration")
    st.latex(r"1s^2\ 2s^2\ 2p^1")
    
    # Orbital Diagram
    orbitals = ["1s", "2s", "2p"]
    electrons = [2, 2, 1]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.barh(orbitals, electrons, color="cyan")
    ax.set_xlabel("Electrons", fontsize=12, color="white")
    ax.set_ylabel("Orbitals", fontsize=12, color="white")
    ax.set_title("Orbital Filling Diagram", fontsize=14, color="white")
    ax.set_xlim(0, 4)

    fig.patch.set_facecolor("#0e1117")
    ax.set_facecolor("#0e1117")
    ax.tick_params(axis="both", colors="white")

    st.pyplot(fig)

    st.divider()

    # ----------------------------------------
    # 📈 Variation of Heat Capacity with Temperature
    # ----------------------------------------
    st.subheader("📈 Heat Capacity vs Temperature")

    temp_range = st.slider("Select Temperature Range (K)", 200, 1500, (300, 1200))

    T = np.linspace(temp_range[0], temp_range[1], 100)
    Cp = 1.02 + 0.0002 * T - 3.1e-8 * T**2  

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(T, Cp, color="orange", linewidth=2, label="Specific Heat Capacity (J/g·K)")
    ax.set_xlabel("Temperature (K)", fontsize=12)
    ax.set_ylabel("Specific Heat Capacity (J/g·K)", fontsize=12)
    ax.set_title("Heat Capacity of Boron vs Temperature", fontsize=14)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)

    fig.patch.set_facecolor("#0e1117")
    ax.set_facecolor("#0e1117")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.title.set_color("white")
    ax.tick_params(colors="white")

    st.pyplot(fig)

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
    
    These allotropes have a unique icosahedral structure, contributing to boron's hardness and thermal resistance.
    """)

    st.divider()

    # ----------------------------------------
    # 🌈 Atomic Spectra
    # ----------------------------------------
    st.subheader("🌈 Atomic Spectra")
    st.write("""
    Boron’s atomic spectrum features strong lines in the ultraviolet (UV) and visible regions:
    - **B II** at **345.10 nm**
    - **B I** at **249.77 nm**
    """)

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


    # Atomic and Ionic Radii
    st.subheader("📏 Atomic and Ionic Radii")
    st.write("Boron has a relatively small atomic radius of 85 pm. When it forms B³⁺, its ionic radius significantly decreases to approximately 23 pm.")
    
    # Electronegativity & Electron Affinity
    st.subheader("🔋 Electronegativity & Electron Affinity")
    st.write("Boron has a relatively high electronegativity of 2.04 and a moderate electron affinity of 26.7 kJ/mol, meaning it tends to attract electrons in chemical bonds.")
    
    # Oxidation States & Reactivity
    st.subheader("🔥 Oxidation States & Reactivity")
    st.write("Boron primarily exhibits a +3 oxidation state. Unlike alkali metals, boron is relatively unreactive but forms strong covalent bonds, especially in borates and boron compounds.")
    
    # Melting & Boiling Points
    st.subheader("🌡️ Melting & Boiling Points")
    st.write("Boron has a high melting point of 2076°C and a boiling point of 3927°C, reflecting its strong covalent bonding.")
    
    # Density & Atomic Volume
    st.subheader("⚖️ Density & Atomic Volume")
    st.write("Boron has a density of 2.34 g/cm³, significantly higher than alkali metals but lower than most transition metals.")
    
    # Isotopes of Boron
    st.subheader("🧪 Isotopes of Boron")
    st.write("Boron has two naturally occurring isotopes: B-10 (19.9%) and B-11 (80.1%). B-10 is used in nuclear reactors and radiation shielding due to its neutron absorption properties.")
    
    # Crystal Structure
    st.subheader("💎 Crystal Structure")
    st.write("Boron has a complex crystalline structure, often existing in allotropes like α-rhombohedral and β-rhombohedral forms, which contribute to its high hardness and brittleness.")

    st.caption("Data Source: [WebElements Periodic Table](https://www.webelements.com/boron/atoms.html)")

    
    
elif a == ":violet[K]  ✨ Potassium":
    
    st.title("🔬 Potassium - Atomic Properties")

    # Atomic properties
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Atomic Number", value="19")
    col2.metric(label="Mass Number", value="39")
    col3.write(" ")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Atomic Radius", value="227 pm")
    col2.metric(label="Ionic Radius (K⁺)", value="138 pm")
    col3.metric(label="Density", value="0.862 g/cm³")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Oxidation States", value="+1")
    col2.metric(label="Electronegativity", value="0.82")
    col3.metric(label="Melting Point", value="63.5°C")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Boiling Point", value="759°C")
    col2.metric(label="Vanderwaals Radius", value="275 pm")
    col3.write(" ")
    
    st.divider()
    
    # Electronic Configuration
    st.subheader("⚙️ Electronic Configuration")
    st.latex("1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹")
    
    st.write("Potassium belongs to Group 1 (Alkali Metals) and has a single electron in its outermost shell (4s¹). This makes it highly reactive, as it readily loses this electron to form K⁺.")
    
    # Orbital Filling Diagram
    orbitals = ["1s", "2s", "2p", "3s", "3p", "4s"]
    electrons = [2, 2, 6, 2, 6, 1]
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(orbitals, electrons, color="#5cde1f")
    ax.set_xlabel("Electrons", fontsize=12, color="white")
    ax.set_ylabel("Orbitals", fontsize=12, color="white")
    ax.set_title("Orbital Filling Diagram", fontsize=14, color="white")
    ax.set_xlim(0, 10)
    
    fig.patch.set_facecolor("#0e1117")
    ax.set_facecolor("#0e1117")
    ax.tick_params(axis="both", colors="white")
    
    st.pyplot(fig)
    
    st.divider()
    
    # Ionization Energy
    st.subheader("⚡ Ionization Energy")
    st.write("Potassium has a low ionization energy, as it easily loses its outermost electron. The first ionization energy is significantly lower than the second because removing a second electron requires breaking a stable noble gas configuration.")
    
    ionization_data = {
        "Ionization Step": ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"],
        "Energy (kJ/mol)": [418.8, 3052, 4419, 5877, 7975, 9590, 11343, 13010]
    }
    
    df_ionization = pd.DataFrame(ionization_data)
    
    fig = px.bar(df_ionization, x="Ionization Step", y="Energy (kJ/mol)",
                 text="Energy (kJ/mol)", color="Energy (kJ/mol)",
                 color_continuous_scale="viridis", height=400)
    
    fig.update_traces(textfont_size=12, textposition="outside")
    fig.update_layout(plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", font_color="white")
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("  ")
    
    # Atomic Spectra
    st.subheader("🌈 Atomic Spectra")
    st.write("Potassium's atomic spectrum features strong emission lines in the visible region")
    st.image("https://atomic-spectra.net/images/K.png?1742227132", caption="Emission Spectrum of Potassium", use_container_width=True)
    
    
    # Atomic and Ionic Radii
    st.subheader("📏 Atomic and Ionic Radii")
    st.write("Potassium has a relatively large atomic radius of 227 pm. When it loses an electron to form K⁺, its radius decreases to 138 pm.")
    
    # Electronegativity & Electron Affinity
    st.subheader("🔋 Electronegativity & Electron Affinity")
    st.write("Potassium has a low electronegativity (0.82) and low electron affinity, indicating its tendency to lose electrons rather than gain them.")
    
    # Oxidation States & Reactivity
    st.subheader("🔥 Oxidation States & Reactivity")
    st.write("Potassium typically exhibits a +1 oxidation state. It is highly reactive, especially with water, forming potassium hydroxide and hydrogen gas.")
    
    # Melting & Boiling Points
    st.subheader("🌡️ Melting & Boiling Points")
    st.write("Potassium has a melting point of 63.5°C and a boiling point of 759°C, making it one of the softer alkali metals.")
    
    # Density & Atomic Volume
    st.subheader("⚖️ Density & Atomic Volume")
    st.write("Potassium has a low density of 0.89 g/cm³, making it lighter than water.")
    
    # Isotopes of Potassium
    st.subheader("🧪 Isotopes of Potassium")
    st.write("Potassium has three naturally occurring isotopes: K-39 (93.3%), K-40 (0.0117%, radioactive), and K-41 (6.7%). K-40 is significant for radiometric dating.")
    
    # Crystal Structure
    st.subheader("💎 Crystal Structure")
    st.write("Potassium crystallizes in a body-centered cubic (BCC) structure, contributing to its malleability and softness.")
    
    st.subheader("🔥 Thermodynamic Properties of Potassium")
    st.write("Heat Capacity (Cp), Enthalpy (H), and Entropy (S) using Shomate Equation")
    
    # Constants for two temperature ranges from the table
    shomate_params = {
        "1039.54 - 1800 K": {"A": 20.66122, "B": 0.391869, "C": -0.417344, "D": 0.145582, "E": 0.003764, "F": 82.83860, "G": 185.2650, "H": 88.99996},
        "1800 - 6000 K": {"A": 58.70570, "B": -27.38277, "C": 6.730509, "D": -0.420844, "E": -25.87921, "F": 32.37931, "G": 198.3777, "H": 88.99996}
    }
    
    # Temperature range selector
    temp_range = st.radio("Select Temperature Range (K):", ["1039.54 - 1800 K", "1800 - 6000 K"])
    T_min, T_max = map(float, temp_range.split(" K")[0].split(" - "))
    
    import numpy as np
    import matplotlib.pyplot as plt
    import streamlit as st
    
    # Sample Temperature values (replace with actual data)
    T_values = np.linspace(1039.54, 1800, 50)
    
    # Given Shomate equation parameters for 1039.54 to 1800 K
    A, B, C, D, E, F, G, H = 20.66122, 0.391869, -0.417344, 0.145582, 0.003764, 82.83860, 185.2650, 88.99996
    
    # Convert temperature to t = T / 1000
    t = T_values / 1000
    
    # Calculate Cp, H, S
    Cp_values = A + B * t + C * t**2 + D * t**3 + E / t**2
    H_values = A * t + (B * t**2) / 2 + (C * t**3) / 3 + (D * t**4) / 4 - E / t + F - H
    S_values = A * np.log(t) + B * t + (C * t**2) / 2 + (D * t**3) / 3 - E / (2 * t**2) + G
    
    
    col1, col2 = st.columns(2)
    # 📌  Plot Cp vs Temperature
    col1.subheader("Cp vs T")
    fig = plt.figure(figsize=(7, 4))
    plt.plot(T_values, Cp_values, label="Heat Capacity (Cp)", color="red")
    plt.xlabel("Temperature (K)", color="white")
    plt.ylabel("Cp (J/mol*K)", color="white")
    plt.title("Heat Capacity vs Temperature", color="white")
    plt.legend()
    plt.grid()
    col1.pyplot(fig)
    
    # 📌 Plot Enthalpy (H) vs Temperature
    col2.subheader("H vs T")
    fig = plt.figure(figsize=(7, 4))
    plt.plot(T_values, H_values, label="Enthalpy (H)", color="blue")
    plt.xlabel("Temperature (K)", color="white")
    plt.ylabel("H (kJ/mol)", color="white")
    plt.title("Enthalpy vs Temperature", color="white")
    plt.legend()
    plt.grid()
    col2.pyplot(fig)
    
    # 📌 Plot Entropy (S) vs Temperature
    col1.subheader("S vs T")
    fig = plt.figure(figsize=(7, 4))
    plt.plot(T_values, S_values, label="Entropy (S)", color="green")
    plt.xlabel("Temperature (K)", color="white")
    plt.ylabel("S (J/mol*K)", color="white")
    plt.title("Entropy vs Temperature", color="white")
    plt.legend()
    plt.grid()
    col1.pyplot(fig)
    
    # Explanation
    st.info("The thermodynamic properties of potassium are calculated using the Shomate equation. Select a temperature range to view the corresponding data.")
    
    
    st.subheader("🔬 Vapor Pressure of Potassium Calculated using Antoine Equation")
    st.write("log10(P) = A - (B / (T + C))")
    # Antoine Equation Parameters for Potassium (from NIST)
    A, B, C = 4.45718, 4691.58, 24.195
    T_min, T_max = 679.4, 1033.0  # Temperature range in K
    
    # User Input for Temperature Range
    T_range = st.slider("Select Temperature Range (K)", min_value=int(T_min), max_value=int(T_max), value=(int(T_min), int(T_max)))
    T_values = np.linspace(T_range[0], T_range[1], 100)
    
    # Compute Vapor Pressure using Antoine Equation
    P_values = 10 ** (A - (B / (T_values + C)))  # Pressure in bar
    
    # Plot the Vapor Pressure vs Temperature
    plt.style.use("ggplot")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(T_values, P_values, label="Vapor Pressure (bar)", color="red", linewidth=2)
    ax.set_xlabel("Temperature (K)", fontsize=12)
    ax.set_ylabel("Vapor Pressure (bar)", fontsize=12)
    ax.set_title("Vapor Pressure of Potassium", fontsize=14)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)
    
    # Dark theme settings
    fig.patch.set_facecolor("#0e1117")
    ax.set_facecolor("#0e1117")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.title.set_color("white")
    ax.tick_params(colors="white")
    ax.spines["top"].set_color("white")
    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["right"].set_color("white")
    
    
    # Display the Plot
    st.pyplot(fig)
    
    # Explanation
    st.info("The vapor pressure of potassium is computed using the Antoine equation with parameters from NIST.")

elif a == ":orange[Kr] 🍀 Krypton" :
    st.title("🔬 Krypton - Atomic Properties")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Atomic Radius", value="88 pm")
    col2.metric(label="Covalent Radius", value="116 pm")
    col3.metric(label="Vanderwaals radius", value="202 pm")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Oxidation states", value="+2, +1")
    col2.metric(label="Electronegativity", value="3.00 ")
    col3.write("  ")
    
    # Force reload to refresh the animati
    
    st.divider()
    
    st.subheader("⚙️ Electronic configuration")
    st.latex("1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶")
    
    st.write("Krypton belongs to Group 18 (Noble Gases), its outermost shell (4p⁶) is completely filled, making it chemically inert. The filled p-orbital gives Krypton high stability, as it does not readily gain or lose electrons.")
    st.write("Krypton’s stable electronic configuration also explains its high ionization energy and low chemical reactivity. However, under extreme conditions, Krypton can form compounds like KrF₂ (Krypton Difluoride), where it donates electrons to highly electronegative fluorine.")
    orbitals = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p"]
    electrons = [2, 2, 6, 2, 6, 2, 10, 6]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(orbitals, electrons, color="#5cde1f")
    ax.set_xlabel("Electrons", fontsize=12, color="white")
    ax.set_ylabel("Orbitals", fontsize=12, color="white")
    ax.set_title("Orbital Filling Diagram", fontsize=14, color="white")
    ax.set_xlim(0, 10)
    
    # Dark theme
    fig.patch.set_facecolor("#0e1117")
    ax.set_facecolor("#0e1117")
    ax.tick_params(axis="both", colors="white")
    
    st.pyplot(fig)
    
    st.divider()
    
    st.subheader("⚡Ionization Energy")
    st.write("Ionization energy is the energy required to remove an electron from a neutral atom in the gaseous state. Krypton, being a noble gas, has a high ionization energy due to its stable electron configuration (full outer shell). Each additional electron removed requires significantly more energy because the atom becomes more positively charged.")
    ionization_data = {
        "Ionization Step": ["1st", "2nd", "3rd", "4th", "5th"],
        "Energy (kJ/mol)": [1350.8, 2350.4, 3565, 5070, 6240]
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
    st.write("Krypton exhibits a complex atomic spectrum due to its multiple electronic transitions. Like other noble gases, it emits distinct spectral lines when excited electrons return to lower energy levels. Krypton's spectrum primarily features sharp emission lines in the visible, ultraviolet (UV), and infrared (IR) regions, making it valuable for scientific and technological applications.")
    st.write("One of Krypton’s most notable spectral lines is the 605.78 nm (orange-red) emission from the krypton-86 isotope, which was historically used to define the meter in 1960. Additionally, krypton emits blue, green, and yellow spectral lines when ionized, contributing to its use in high-intensity gas discharge lamps and lasers.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/36_%28Kr_I%29_NIST_ASD_emission_spectrum.png/1920px-36_%28Kr_I%29_NIST_ASD_emission_spectrum.png", use_container_width=True)
    
    st.divider()
