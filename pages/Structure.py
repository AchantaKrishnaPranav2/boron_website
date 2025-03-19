import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Structure",
    page_icon="🧩",
)
a = st.radio(
    "Choose an element to explore:",
    [":red[B]  🔥 Boron", ":violet[K]  ✨ Potassium",  ":orange[Kr] 🍀 Krypton"],
    index=None)
if a == ":red[B]  🔥 Boron":
    st.title("🧩 Boron - Structure")
    
    st.info("""
    Boron has a **unique covalent network structure**, making it different from metals and nonmetals.  
    The most common **crystalline form** consists of **icosahedral B₁₂ clusters**, forming complex lattice structures.  
    This icosahedral arrangement gives boron **high hardness and thermal stability**.
    """)
    
    st.caption("Source: [Royal Society of Chemistry](https://www.rsc.org/periodic-table/element/5/boron)")
    
    st.divider()
    
    # 🔹 Icosahedral Boron Structure
    st.subheader("🔹 Icosahedral Boron Structure")
    
    st.write("""
    The **icosahedral (B₁₂) structure** is the fundamental unit of **crystalline boron**.  
    It consists of **12 boron atoms** arranged in a polyhedron with 20 triangular faces.  
    This structure enhances **mechanical strength, chemical stability, and high melting points**.
    """)
    
    fig = go.Figure()
    
    # Define Boron atom positions in an icosahedral structure
    vertices = [
        (0, 0, 1), (0, 0, -1), (0.894, 0, 0.447), (-0.894, 0, 0.447),
        (0.276, 0.851, 0.447), (-0.276, 0.851, 0.447), (0.276, -0.851, 0.447),
        (-0.276, -0.851, 0.447), (0.724, 0.526, -0.447), (-0.724, 0.526, -0.447),
        (0.724, -0.526, -0.447), (-0.724, -0.526, -0.447)
    ]
    
    # Add Boron atoms
    fig.add_trace(go.Scatter3d(
        x=[v[0] for v in vertices], y=[v[1] for v in vertices], z=[v[2] for v in vertices],
        mode='markers', marker=dict(size=8, color="cyan", opacity=0.8), name="Boron Atoms"
    ))
    
    # Define edges to connect the atoms in an icosahedral shape
    edges = [
        (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 8), (1, 9), (1, 10), (1, 11),
        (1, 2), (1, 3), (2, 4), (2, 6), (3, 5), (3, 7), (4, 8), (4, 9), (5, 8), (5, 10),
        (6, 9), (6, 11), (7, 10), (7, 11), (8, 10), (8, 9), (9, 11), (10, 11)
    ]
    
    # Add lines connecting the vertices
    for edge in edges:
        fig.add_trace(go.Scatter3d(
            x=[vertices[edge[0]][0], vertices[edge[1]][0]],
            y=[vertices[edge[0]][1], vertices[edge[1]][1]],
            z=[vertices[edge[0]][2], vertices[edge[1]][2]],
            mode='lines', line=dict(color="white", width=2), showlegend=False
        ))
    
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False), 
            bgcolor="black"
        ),
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor="black",
        font=dict(color="white")
    )
    
    st.plotly_chart(fig, use_container_width=True)
    

    st.caption("Source: [Wikipedia - Boron](https://en.wikipedia.org/wiki/Boron)")
    import streamlit as st

    # Boron's Crystal Structure
    st.subheader("🔹 Why does Boron have a Complex Structure?")
    col1, col2, col3 = st.columns(3)
    
    col1.markdown("<h5 style='color:#ff5733; text-align: center;'>Covalent Bonding</h5>", unsafe_allow_html=True)
    col1.write("Boron forms strong covalent bonds, leading to complex icosahedral structures instead of simple BCC or FCC.")
    
    col2.markdown("<h5 style='color:#ff5733; text-align: center;'>High Melting Point</h5>", unsafe_allow_html=True)
    col2.write("Due to strong bonding, boron has a very high melting point (~2076°C), making it structurally rigid.")
    
    col3.markdown("<h5 style='color:#ff5733; text-align: center;'>Allotropic Forms</h5>", unsafe_allow_html=True)
    col3.write("Boron exists in multiple crystalline and amorphous forms, including α-Boron and β-Boron.")
    
    st.divider()
    
    # Mechanical Properties of Boron
    st.subheader("🔹 Young’s Modulus of Boron")
    st.write("**Young's Modulus of Boron:** 450 GPa")
    st.write("🔹 **Application:** Used in **high-strength aerospace materials** and **lightweight structural components**.")
    
    st.subheader("🔹 Bulk Modulus of Boron")
    st.write("**Bulk Modulus of Boron:** 320 GPa")
    st.write("🔹 **Application:** Used in **boron carbide armor** and **cutting tools** due to its high incompressibility.")
    
    st.subheader("🔹 Shear Modulus of Boron")
    st.write("**Shear Modulus of Boron:** 190 GPa")
    st.write("🔹 **Application:** Used in **high-rigidity composites** like **Boron fiber-reinforced polymers** for aircraft.")
    

elif a == ":violet[K]  ✨ Potassium":
    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    
    
    
    st.title("🧩 Potassium - Structure")
    st.info("Potassium is an alkali metal that crystallizes in a **body-centered cubic (BCC)** structure under standard conditions. Its atomic structure influences its electrical conductivity, malleability, and chemical reactivity.")
    
    # User selection for structure type
    structure_type = "BCC (Standard)"
    
    # Define lattice points for BCC, FCC, and Simple Cubic structures
    def get_lattice_points(structure):
        if structure == "BCC (Standard)":
            return np.array([
                [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1],
                [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1],
                [0.5, 0.5, 0.5]  # Center atom (BCC-specific)
            ])
    
    lattice_points = get_lattice_points(structure_type)
    
    # Define cube edges
    edges = [
        (0, 1), (1, 4), (4, 2), (2, 0),  # Bottom face
        (3, 5), (5, 7), (7, 6), (6, 3),  # Top face
        (0, 3), (1, 5), (2, 6), (4, 7)   # Vertical edges
    ]
    
    # Create 3D figure
    fig = go.Figure()
    
    # Add Potassium atoms as scatter points
    fig.add_trace(go.Scatter3d(
        x=lattice_points[:, 0], y=lattice_points[:, 1], z=lattice_points[:, 2],
        mode='markers', marker=dict(size=15, color="orange", opacity=1, symbol="circle"),
        name="Potassium Atoms"
    ))
    
    # Add cube edges
    for edge in edges:
        p1, p2 = lattice_points[edge[0]], lattice_points[edge[1]]
        fig.add_trace(go.Scatter3d(
            x=[p1[0], p2[0]], y=[p1[1], p2[1]], z=[p1[2], p2[2]],
            mode='lines', line=dict(color="white", width=3),
            showlegend=False
        ))
    
    # Customize layout
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor="black"
        ),
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor="black",
        font=dict(color="white")
    )
    
    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    st.subheader("🔹Why does Potassium have BCC Structure?")
    col1, col2, col3 = st.columns(3)
    col1.markdown("<h5 style='color:#ffcc00; text-align: center;'>Low-Density Packing</h5>", unsafe_allow_html=True)
    col1.write("BCC packing is not as dense as FCC, which makes potassium relatively soft and malleable.")
    col2.markdown("<h5 style='color:#ffcc00; text-align: center;'>Electropositive Nature</h5>", unsafe_allow_html=True)
    col2.write("Potassium readily donates electrons, leading to weak metallic bonding, favoring BCC.")
    col3.markdown("<h5 style='color:#ffcc00; text-align: center;'>Temperature Dependency</h5>", unsafe_allow_html=True)
    col3.write("Under high pressure, potassium can transition to FCC or other structures.")
    st.divider()
    st.subheader("🔹youngs modulus of potassium:")
    st.write("**Young's Modulus of Potassium:** 3.53 GPa")
    st.subheader("🔹bulk modulus of potassium:")
    st.write("**bulk Modulus of Potassium:** 3.1 GPa")
    st.subheader("🔹shear modulus of potassium:")
    st.write("**shear Modulus of Potassium:** 1.3 GPa")

elif a == ":orange[Kr] 🍀 Krypton" :
    st.title("🧩 Krypton - Structure")
    st.info("Krypton is a noble gas, which means that under standard temperature and pressure (STP), it exists as a monatomic gas. However, krypton can solidify under extremely low temperatures and high pressures. When it becomes a solid, it adopts a **face-centered cubic (FCC)** crystal structure.")
    
    st.markdown("<h3 style='color:#9ef33e; text-align: center;'>FCC Structure of Solid Krypton</h3>", unsafe_allow_html=True)
    
    # FCC lattice points
    fcc_points = np.array([
        [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1],
        [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1],
        [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5],
        [0.5, 0.5, 1], [0.5, 1, 0.5], [1, 0.5, 0.5]
    ])
    
    # Define cube edges (external edges only)
    edges = [
        (0, 1), (1, 4), (4, 2), (2, 0),  # Bottom face
        (3, 5), (5, 7), (7, 6), (6, 3),  # Top face
        (0, 3), (1, 5), (2, 6), (4, 7)   # Vertical edges
    ]
    
    # Create 3D figure
    fig = go.Figure()
    
    # Add Krypton atoms as scatter points
    fig.add_trace(go.Scatter3d(
        x=fcc_points[:, 0], y=fcc_points[:, 1], z=fcc_points[:, 2],
        mode='markers', marker=dict(size=15, color="cyan", opacity=1, symbol="circle"),
        name="Krypton Atoms"
    ))
    
    # Add cube edges
    for edge in edges:
        p1, p2 = fcc_points[edge[0]], fcc_points[edge[1]]
        fig.add_trace(go.Scatter3d(
            x=[p1[0], p2[0]], y=[p1[1], p2[1]], z=[p1[2], p2[2]],
            mode='lines', line=dict(color="white", width=3),
            showlegend=False
        ))
    
    # Customize layout
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor="black"
        ),
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor="black",
        font=dict(color="white")
    )
    
    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    st.info("Lattice constant : a = 583.57 pm")
    
    st.divider()
    
    st.subheader("🌀  Other Properties for Krypton")
    table_data = {
        "Property": ["Thermal Conductivity (W / m.K)", "Magnetic Ordering", "Molar magnetic susceptibility (cm³/mol)", "Speed of sound in gas (m/s)", "Speed of sound in liquid (m/s)"],
        "Value": ["0.00943", "Diamagnetic", "-0.0000286", "221", "1120"],
    }
    st.dataframe(table_data, hide_index=True)
    st.divider()
    
    st.subheader("🔹Why does Krypton have FCC Structure ?")
    col1, col2, col3 = st.columns(3)
    col1.markdown("<h5 style='color:#9ef33e; text-align: center;'>Weak Intermolecular Forces (Van der Waals Forces)</h5>", unsafe_allow_html=True)
    col1.write("Krypton atoms do not form strong chemical bonds due to their full outer electron shell. The only forces holding solid krypton together are Van der Waals forces (weak London dispersion forces).")
    col2.markdown("<h5 style='color:#9ef33e; text-align: center;'>FCC is Common for Noble Gases in Solid Form</h5>", unsafe_allow_html=True)
    col2.write("  ")
    col2.write("Other noble gases like argon (Ar), neon (Ne), and xenon (Xe) also crystallize in an FCC structure when solid. The FCC structure allows efficient packing of spherical atoms with minimal repulsion.")
    col3.markdown("<h5 style='color:#9ef33e; text-align: center;'>Solidification at very Low-Temperature</h5>", unsafe_allow_html=True)
    col3.write("  ")
    col3.write("Krypton solidifies at 115.79 K (-157.36°C, -251.25°F) under atmospheric pressure. At these temperatures, thermal energy is low, allowing the weak Van der Waals interactions to hold atoms in an FCC lattice.")
    
    st.divider()
    
    st.subheader("📚Structure of other compounds of Krypton")
    col1, col2 = st.columns(2)
    col2.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Krypton_hydride_structure.png/330px-Krypton_hydride_structure.png")
    col1.write("Kr(H₂)₄ is a solid-state compound formed under high-pressure conditions where krypton atoms (Kr) trap hydrogen molecules (H₂) in a unique crystalline structure. This compound is classified as a van der Waals (or clathrate-like) solid, meaning that the krypton atoms act as a host and the hydrogen molecules behave as guests.")
    col1.write("The krypton atoms form an octahedral arrangement within the crystal lattice."
     +"This means each krypton atom is surrounded by six neighboring krypton atoms, forming an FCC (face-centered cubic) substructure.")
    
    st.divider()
