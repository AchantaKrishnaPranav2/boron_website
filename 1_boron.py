import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Boron Properties",
    page_icon="🧪",
    layout="wide"
)

# Radio button selection
a = st.radio(
    "Choose an element to explore:",
    [":red[B]  🔥 Boron", ":violet[K]  ✨ Potassium"],
    index=None
)

# Main content
if a == ":red[B]  🔥 Boron":
    st.markdown("# **Welcome to the World of Boron** 🧪")
    st.write("Explore the fascinating properties, occurrence, and uses of Boron.")

    st.markdown("<h1 style='color:#ffffff;'>🧪 Boron: A Unique Metalloid</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 2])
    col1.image("https://upload.wikimedia.org/wikipedia/commons/1/19/Boron_R105.jpg", caption="Boron (β-rhombohedral)")
    col2.markdown(
        '''
        <style>
        .big-font {
            font-size: 16px !important;
            color: white;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
    col2.markdown('<p class="big-font">Boron (B) is a metalloid in Group 13 of the periodic table. It has properties of both metals and non-metals.</p>', unsafe_allow_html=True)
    col2.markdown('<p class="big-font">It is essential in industries like glassmaking, agriculture, and electronics.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    col1.info("**Atomic number - 5**")
    col1.info("**Atomic mass - 10.81**")
    col1.info("**Group - 13 (Metalloids)**")
    col2.info("**Number of protons - 5**")
    col2.info("**Number of neutrons - 6 (most common isotope)**")
    col2.info("**Period - 2**")

    st.divider()

    st.header("📋 Physical Properties")
    st.info("Boron is a hard, black, and brittle material. It has high melting and boiling points.")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Phase at STP", value="Solid")
    col2.metric(label="Melting point", value="2349 K")
    col3.metric(label="Boiling point", value="4200 K")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Density", value="2.34 g/cm³")
    col2.metric(label="Heat of fusion", value="50.2 kJ/mol")
    col3.metric(label="Heat of vaporization", value="480 kJ/mol")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Thermal Conductivity", value="27 W/m·K")
    col2.metric(label="Specific Heat Capacity", value="1.02 J/g·K")
    col3.metric(label="Refractive Index", value="2.46 (crystalline)")

    # Plotting Boron Vapor Pressure
    Temp = np.array([1000, 2000, 3000, 4000, 5000])
    pressure = np.array([0.1, 1, 10, 100, 1000])
    plt.style.use("seaborn-v0_8-dark")
    fig, ax = plt.subplots(figsize=(7, 4), facecolor="#0e1117")
    ax.plot(Temp, pressure, '.-', color="#e81753", linewidth=2, marker="o", markersize=4, markerfacecolor="white", markeredgecolor="#5cde1f", alpha=0.8)

    ax.set_facecolor("#0e1117")  # Dark background
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("white")
    ax.spines["bottom"].set_color("white")

    ax.xaxis.label.set_color("white")  
    ax.yaxis.label.set_color("white")  
    ax.tick_params(axis="x", colors="white")  
    ax.tick_params(axis="y", colors="white")  

    ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.5)

    ax.set_title(f"Vapor Pressure Variation with Temperature", fontsize=14, fontweight="bold", color="white")
    ax.set_xlabel(f"Temperature (in K)", fontsize=12, fontweight="bold")
    ax.set_ylabel("Pressure (in Pa)", fontsize=12, fontweight="bold")
    st.pyplot(fig)

    st.divider()

    # Boron Discoverers with Images
    st.markdown("<h1 style='color:#ffffff;'>🧑‍🔬 Discovery of Boron</h1>", unsafe_allow_html=True)
    
    st.info("Boron was discovered in 1808 by three scientists: **Humphry Davy, Joseph Louis Gay-Lussac, and Louis Jacques Thénard**.")
    
    col1, col2, col3 = st.columns(3)
    col1.image("https://cdn.britannica.com/96/12396-050-A1110D81/Humphry-Davy-Thomas-Lawrence-detail-oil-painting.jpg", caption="Sir Humphry Davy",height = 100)
    col2.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Gaylussac.jpg/338px-Gaylussac.jpg", caption="Joseph Louis Gay-Lussac",height = 100)
    col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Louis_Jacques_Th%C3%A9nard.jpg/330px-Louis_Jacques_Th%C3%A9nard.jpg", caption="Louis Jacques Thénard,height = 100")
    
    st.write("Boron was first isolated in 1808 through electrolysis by **Humphry Davy**, and independently by **Joseph Gay-Lussac and Louis Thenard**. It is found naturally in borax and is widely used in various industries today.")

    st.divider()

    # Uses of Boron
    with st.expander("🔬 **Applications of Boron**"):
        st.write(
            """
            The **primary application** of boron is in **boron filaments**,  
            which have **high-strength properties** similar to **carbon fibers**.
            """
        )
        st.success("🔧 **Boron’s Role**: Used in aerospace, bulletproof vests, and composite materials!")

    # Fun Facts
    st.markdown("<h2 style='color:#ffffff;'>💡 Fun Facts about Boron</h2>", unsafe_allow_html=True)
    st.info("✅ Boron is essential for plant growth but toxic in high amounts!")
    st.info("✅ **Boron carbide** (B₄C) is used in tank armor and bulletproof vests.")
    st.info("✅ **Boron nitride** is as hard as diamond but lubricates like graphite.")

    st.divider()

    st.markdown("🚀 **Explore More:** [Wikipedia - Boron](https://en.wikipedia.org/wiki/Boron)")

