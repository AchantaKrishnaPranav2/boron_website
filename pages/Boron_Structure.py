
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Boron - Structure",
    page_icon="🧩",
)

st.title("🧩 Boron - Structure")
st.info("Boron has a complex **covalent network structure**. The most common form is amorphous boron or crystalline boron with an **icosahedral arrangement**.")

st.subheader("🔹 Icosahedral Boron Structure")
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
    mode='markers', marker=dict(size=8, color="cyan"), name="Boron Atoms"
))

fig.update_layout(
    scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False), bgcolor="black"),
    margin=dict(l=0, r=0, t=30, b=0),
    paper_bgcolor="black",
    font=dict(color="white")
)

st.plotly_chart(fig, use_container_width=True)
