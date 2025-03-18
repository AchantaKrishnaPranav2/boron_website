import streamlit as st

st.set_page_config(
    page_title="Boron - Occurrences and Applications",
    page_icon="🔎",
)

st.title("🔎 Boron - Occurrences and Applications")

# 🔍 Natural Occurrence of Boron
st.subheader("🌍 Natural Occurrence of Boron")
st.write("""
Boron is primarily found in **borate minerals**, commonly extracted from **Turkey, the USA, and Argentina**.  
The major boron-containing minerals include:
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/dd/Borax_3D.png", caption="Borax (Na₂B₄O₇·10H₂O)")
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/11/Kernite-212887.jpg", caption="Kernite", use_container_width=True)
with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5e/Colemanite_1.jpg", caption="Colemanite", use_container_width=True)

st.write("""
- **Borax (Na₂B₄O₇·10H₂O)** – A widely used source of boron.
- **Kernite (Na₂B₄O₇·4H₂O)** – A hydrated form of borax.
- **Colemanite (CaB₃O₄(OH)₃·H₂O)** – A common borate mineral in sedimentary deposits.
""")

st.caption("Data Source: [Wikipedia - Boron](https://en.wikipedia.org/wiki/Boron)")

st.divider()

# ⚙️ Applications of Boron
st.subheader("⚙️ Applications of Boron")
st.write("Boron has diverse applications across multiple industries. Below are some key uses:")

# 📌 Glass & Ceramics
st.image("https://upload.wikimedia.org/wikipedia/commons/c/cb/Borosilicate_glass_pipette.jpg", caption="Borosilicate Glass", use_container_width=True)
st.markdown("""
### **📌 Glass and Ceramics**
- **Borosilicate glass** (Pyrex) is highly **heat-resistant** and used in lab equipment, cookware, and telescopes.
- Adds **mechanical strength** to ceramics.
""")

# ⚛️ Nuclear Reactors
st.image("https://upload.wikimedia.org/wikipedia/commons/1/1d/Nuclear_reactor_core.jpg", caption="Nuclear Reactor Control Rods", use_container_width=True)
st.markdown("""
### **⚛️ Nuclear Reactors**
- **Boron-10** is an excellent **neutron absorber**, used in **nuclear reactor control rods**.
- Helps regulate nuclear fission reactions and prevents meltdowns.
""")

# 🧴 Detergents & Bleaches
st.image("https://upload.wikimedia.org/wikipedia/commons/9/93/Washing_Powder.jpg", caption="Boron in Detergents", use_container_width=True)
st.markdown("""
### **🧴 Detergents & Bleaches**
- **Sodium perborate** is a key ingredient in **laundry detergents and bleaches**.
- Acts as a **whitening and stain-removal agent**.
""")

# 🌱 Agriculture
st.image("https://upload.wikimedia.org/wikipedia/commons/7/72/Boron_deficiency_in_plants.jpg", caption="Boron Deficiency in Plants", use_container_width=True)
st.markdown("""
### **🌱 Agriculture**
- **Boron is an essential micronutrient** for plants.
- Deficiency leads to **stunted growth and poor fruit development**.
""")

# 💻 Electronics
st.image("https://upload.wikimedia.org/wikipedia/commons/3/3e/Semiconductor_wafer.jpg", caption="Boron in Semiconductors", use_container_width=True)
st.markdown("""
### **💻 Electronics**
- Used in **semiconductor doping** (Boron-doped silicon).
- Enhances the efficiency of **solar cells and microchips**.
""")

st.caption("Information Source: [Periodic Table - Royal Society of Chemistry](https://periodic-table.rsc.org/element/5/boron)")

st.divider()
