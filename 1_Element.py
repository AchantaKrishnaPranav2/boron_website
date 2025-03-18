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

    st.divider()

    # Graph: Vapor Pressure vs Temperature
    Temp = np.array([1000, 2000, 3000, 4000, 5000])
    pressure = np.array([0.1, 1, 10, 100, 1000])

    fig, ax = plt.subplots(figsize=(7, 4), facecolor="#0e1117")
    ax.plot(Temp, pressure, '.-', color="#e81753", linewidth=2, marker="o", markersize=4, markerfacecolor="white", markeredgecolor="#5cde1f", alpha=0.8)

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

    ax.set_title(f"Vapor Pressure Variation with Temperature", fontsize=14, fontweight="bold", color="white")
    ax.set_xlabel(f"Temperature (K)", fontsize=12, fontweight="bold")
    ax.set_ylabel("Pressure (Pa)", fontsize=12, fontweight="bold")
    st.pyplot(fig)

    st.divider()

    # Graph: Thermal Conductivity vs Temperature
    Temp_TC = np.array([300, 600, 900, 1200, 1500, 1800])
    TC_values = np.array([27, 25, 22, 20, 18, 15])

    fig, ax = plt.subplots(figsize=(7, 4), facecolor="#0e1117")
    ax.plot(Temp_TC, TC_values, '.-', color="yellow", linewidth=2, marker="o", markersize=4, markerfacecolor="white", markeredgecolor="yellow", alpha=0.8)

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

    ax.set_title("Thermal Conductivity vs Temperature", fontsize=14, fontweight="bold", color="white")
    ax.set_xlabel("Temperature (K)", fontsize=12, fontweight="bold")
    ax.set_ylabel("Thermal Conductivity (W/m·K)", fontsize=12, fontweight="bold")

    st.pyplot(fig)

    st.divider()

    # Table: Boron Allotropes
    st.header("🔬 Boron Allotropes")
    st.write(
        """
        Boron exists in multiple **allotropic forms**, with varying **crystalline structures**.
        The most common allotropes are listed below:
        """
    )
    
    allotropes = {
        "Allotrope": ["α-rhombohedral", "β-rhombohedral", "β-tetragonal", "Amorphous"],
        "Structure": ["Rhombohedral", "Rhombohedral", "Tetragonal", "Non-crystalline"],
        "Stability": ["High", "Very High", "Moderate", "Low"],
        "Density (g/cm³)": [2.46, 2.34, 2.37, "Variable"]
    }

    st.table(allotropes)

    st.divider()

    # Fun Facts
    st.markdown("<h2 style='color:#ffffff;'>💡 Fun Facts about Boron</h2>", unsafe_allow_html=True)
    st.info("✅ Boron is essential for plant growth but toxic in high amounts!")
    st.info("✅ **Boron carbide** (B₄C) is used in tank armor and bulletproof vests.")
    st.info("✅ **Boron nitride** is as hard as diamond but lubricates like graphite.")

    st.divider()
     # Boron Discoverers with Images
    st.markdown("<h1 style='color:#ffffff;'>🧑‍🔬 Discovery of Boron</h1>", unsafe_allow_html=True)
    
    st.info("Boron was discovered in 1808 by three scientists: **Humphry Davy, Joseph Louis Gay-Lussac, and Louis Jacques Thénard**.")
    
    col1, col2, col3 = st.columns(3)
    col1.image("https://cdn.britannica.com/96/12396-050-A1110D81/Humphry-Davy-Thomas-Lawrence-detail-oil-painting.jpg", caption="Sir Humphry Davy",width = 200)
    col2.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Gaylussac.jpg/338px-Gaylussac.jpg", caption="Joseph Louis Gay-Lussac",width = 200)
    col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Louis_Jacques_Th%C3%A9nard.jpg/330px-Louis_Jacques_Th%C3%A9nard.jpg", caption="Louis Jacques Thénard",width = 200)
    
    st.write("Boron was not recognized as an element until it was isolated by Sir Humphry Davy and by Joseph Louis Gay-Lussac and Louis Jacques Thénard. ")
    st.write("In 1808 Davy observed that electric current sent through a solution of borates produced a brown precipitate on one of the electrodes.  ")
    st.write("In his subsequent experiments, he used potassium to reduce boric acid instead of electrolysis. ")
    st.write("He produced enough boron to confirm a new element and named it boracium. ")
    st.write("Gay-Lussac and Thénard used iron to reduce boric acid at high temperatures. ")
    st.write("By oxidizing boron with air, they showed that boric acid is its oxidation product. ")
    st.divider()
    st.write("Jöns Jacob Berzelius identified it as an element in 1824. ")
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/J%C3%B6ns_Jacob_Berzelius_x_Johan_Way.jpg/330px-J%C3%B6ns_Jacob_Berzelius_x_Johan_Way.jpg",caption = "Jöns Jacob Berzelius")
    st.divider()
    st.write("Pure boron was arguably first produced by the American chemist Ezekiel Weintraub in 1909.")

    st.divider()
    st.markdown("🚀 **Explore More:** [Wikipedia - Boron](https://en.wikipedia.org/wiki/Boron)")
elif a == ":violet[K]  ✨ Potassium":

    st.markdown("<h1 style='color:#ffffff;'>🧪 Potassium: A Reactive Alkali Metal</h1>", unsafe_allow_html=True)
    st.sidebar.success("Select a page")
    
    col1, col2 = st.columns([1.2, 2])
    col1.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Potassium.JPG/255px-Potassium.JPG")
    col2.markdown(
        """
        <style>
        .big-font {
            font-size: 16px !important;
            font-weight: ;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    col2.markdown('<p class="big-font">Potassium (K) is a highly reactive alkali metal in Group 1 of the periodic table. It is soft, silvery-white, and easily oxidizes in air.</p>', unsafe_allow_html=True)
    col2.markdown('<p class="big-font">It is an essential element for life, playing a vital role in nerve function, muscle contraction, and fluid balance in organisms.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1,1])
    col1.info("**Atomic number - 19**")
    col1.info("**Atomic mass - 39.098**")
    col1.info("**Group - 1 (Alkali metals)**")
    col2.info("**Number of protons - 19**")
    col2.info("**Number of neutrons - 20**")
    col2.info("**Period - 4**")
    
    st.divider()
    st.header("atom animation")
    st.image("https://i.pinimg.com/originals/5b/96/74/5b96749cd559ef4732536d19f648a732.gif",caption="potassium atom animation")
    st.header("📋 Physical Properties")
    st.info("Soft, silvery-white metal that reacts violently with water, producing hydrogen gas and heat.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Phase at STP", value="Solid")
    col2.metric(label="Melting point", value="336.7 K")
    col3.metric(label="Boiling point", value="1032 K")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Density", value="0.862 g/cm³")
    col2.metric(label="Heat of fusion", value="2.33 kJ/mol")
    col3.metric(label="Heat of vaporization", value="76.9 kJ/mol")
    
    st.write("  ")
    
    # Plotting Potassium Vapor Pressure
    Temp = np.array([300, 400, 500, 600, 700, 800])
    pressure = np.array([0.01, 0.1, 1, 10, 100, 1000])
    plt.style.use("seaborn-v0_8-dark")
    fig, ax = plt.subplots(figsize=(7, 4), facecolor="#0e1117")
    ax.plot(Temp, pressure,  '.-', color="#e81753", linewidth=2, marker="o", markersize=4, markerfacecolor="white", markeredgecolor="#5cde1f", alpha=0.8)
    
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
    
    ax.set_title(f"Vapour Pressure Variation with Temperature", fontsize=14, fontweight="bold", color="white")
    ax.set_xlabel(f"Temperature (in K)", fontsize=12, fontweight="bold")
    ax.set_ylabel("Pressure (in Pa)", fontsize=12, fontweight="bold")
    st.pyplot(fig)
    
    st.divider()
    
    st.markdown("<h1 style='color:#ffffff;'>🪶 History</h1>", unsafe_allow_html=True)
    st.info("Potassium was discovered in 1807 by **Humphry Davy**, using electrolysis on potash.")
    
    col1, col2 = st.columns([2, 1])
    col2.image("https://cdn.britannica.com/96/12396-050-A1110D81/Humphry-Davy-Thomas-Lawrence-detail-oil-painting.jpg?w=300", caption = "Sir Humphry Davy, discoverer of potassium.")
    col1.write("Potassium was first isolated by Sir Humphry Davy in 1807 through the electrolysis of molten potassium hydroxide (KOH). ")
    col1.write("It was the first metal to be isolated using electrolysis, and this technique later led to the discovery of other alkali and alkaline earth metals, including sodium and calcium.")
    col1.write("Potassium compounds such as potash (K₂CO₃) were used in glassmaking, soap production, and fertilizers long before the element was purified. Today, potassium remains essential in industries, agriculture, and biological systems.")
    
    st.divider()

else:
    



    st.markdown("""
    ### 📚 Project Submission
    ---
    **Course:** [Your Course Name]  
    **Professor:** [Professor's Name]  
    **Group Name:** [Your Group Name]  

    **👥 Team Members:**  
    - [Member 1 Name]  
    - [Member 2 Name]  
    - [Member 3 Name]  
    """)

    # Optional: Add a success message or a separator
    st.success("Submission completed successfully!")
    st.divider()  # Adds a horizontal line
