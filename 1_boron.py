import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(
        page_title="Boron Properties",
        page_icon="🧪",
    )
a = st.radio("Choose", [":red[B]  :fire:", ":violet[K]  :sparkles:"], captions=["Boron", "Potassium"], index=None)
if a == ":violet[K]  :sparkles:":
    
    
    
    st.markdown("# Welcome to Boron Properties")
    st.sidebar.success("Select a page above.")
    
    st.write("""
    This website provides detailed insights into Boron’s properties, isotopes, atomic structure, and applications.  
    Use the sidebar to navigate through different sections.
    """)
    st.markdown("<h1 style='color:#ffffff;'>🧪 Boron: A Unique Metalloid</h1>", unsafe_allow_html=True)
    st.sidebar.success("Select a page")
    
    col1, col2 = st.columns([1.2, 2])
    col1.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Boron.jpg")
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
    
    col1, col2 = st.columns([1,1])
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
    
    st.write("  ")
    
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
    
    st.markdown("<h1 style='color:#ffffff;'>🪶 History</h1>", unsafe_allow_html=True)
    st.info("Boron was discovered in 1808 by **Humphry Davy and Joseph Gay-Lussac**.")
    col1, col2 = st.columns([2, 1])
    col2.image("https://cdn.britannica.com/96/12396-050-A1110D81/Humphry-Davy-Thomas-Lawrence-detail-oil-painting.jpg", caption="Sir Humphry Davy, one of the discoverers of Boron.")
    col1.write("Boron was first isolated in 1808 through electrolysis by Humphry Davy and independently by Joseph Gay-Lussac and Louis Thenard. It is found naturally in borax and is used in various industrial applications today.")
