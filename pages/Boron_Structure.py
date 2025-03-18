
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Boron - Structure",
    page_icon="🧩",
)

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
