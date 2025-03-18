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
    import pygame
    import math
    
    # Initialize Pygame
    pygame.init()
    
    # Constants
    WIDTH, HEIGHT = 300, 200  # Small size
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TEXT_COLOR = (0, 255, 0)
    FPS = 60
    
    # Create window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Backroom Engineers Logo")
    
    # Load gear image
    gear = pygame.image.load("data:image/png;base64,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")  # You need to add a small gear image
    gear = pygame.transform.scale(gear, (50, 50))  # Resize the gear
    
    # Font setup
    font = pygame.font.Font(None, 24)  # Small readable font
    
    # Animation variables
    angle = 0
    text_x = WIDTH // 2
    direction = 1  # Text movement direction
    
    # Game loop
    running = True
    clock = pygame.time.Clock()
    
    while running:
        screen.fill(BLACK)
    
        # Rotate gear
        rotated_gear = pygame.transform.rotate(gear, angle)
        gear_rect = rotated_gear.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(rotated_gear, gear_rect.topleft)
    
        # Moving text
        text_surface = font.render("Backroom Engineers", True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(text_x, HEIGHT - 50))
        screen.blit(text_surface, text_rect)
    
        # Update animation
        angle += 3  # Rotate gear
        text_x += direction * 2  # Move text
        if text_x > WIDTH - 60 or text_x < 60:
            direction *= -1  # Reverse direction
    
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

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
