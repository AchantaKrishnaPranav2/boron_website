import streamlit as st

st.set_page_config(
    page_title="Boron - Occurrences and Applications",
    page_icon="🔎",
)

st.title("🔎 Boron - Occurrences and Applications")

# 🔍 Natural Occurrence of Boron
st.subheader("🌍 Natural Occurrence of Boron")
st.write("""
Boron is a **relatively rare element** in Earth's crust, primarily found in **borate minerals** rather than in its pure elemental form.  
Due to its high solubility, boron is commonly concentrated in **evaporite deposits** formed from ancient lakes and seas.  
The **largest boron reserves** are found in **Turkey, the United States, Argentina, Russia, and China**. 

The primary minerals containing boron include:
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/dd/Borax_3D.png", caption="Borax (Na₂B₄O₇·10H₂O)", use_container_width=True)
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/11/Kernite-212887.jpg", caption="Kernite", use_container_width=True)
with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5e/Colemanite_1.jpg", caption="Colemanite", use_container_width=True)

st.write("""
- **Borax (Na₂B₄O₇·10H₂O)** – The most commercially significant boron mineral, used in a variety of industries.  
- **Kernite (Na₂B₄O₇·4H₂O)** – A hydrated form of borax, often found in sedimentary deposits.  
- **Colemanite (CaB₃O₄(OH)₃·H₂O)** – A calcium borate mineral commonly used in **glass and ceramics manufacturing**.
""")

st.caption("Data Source: [Wikipedia - Boron](https://en.wikipedia.org/wiki/Boron)")

st.divider()

# ⚙️ Applications of Boron
st.subheader("⚙️ Applications of Boron")
st.write("Boron is a versatile element with applications in diverse fields, ranging from **industries and agriculture** to **biological functions**.")

# 📌 Glass & Ceramics
st.image("https://upload.wikimedia.org/wikipedia/commons/c/cb/Borosilicate_glass_pipette.jpg", caption="Borosilicate Glass", use_container_width=True)
st.markdown("""
### **📌 Glass and Ceramics**
Boron is an essential component of **borosilicate glass**, known for its **thermal resistance and durability**.  
It is widely used in **laboratory glassware, cookware (like Pyrex), and telescope lenses**.  
Additionally, boron compounds improve the **strength and chemical resistance** of ceramics, making them ideal for **high-temperature applications**.
""")

# ⚛️ Nuclear Reactors
st.image("https://upload.wikimedia.org/wikipedia/commons/1/1d/Nuclear_reactor_core.jpg", caption="Nuclear Reactor Control Rods", use_container_width=True)
st.markdown("""
### **⚛️ Nuclear Reactors**
One of boron's most critical roles is in **nuclear technology**.  
Boron-10, an isotope of boron, has an **exceptional ability to absorb neutrons**, making it an essential component in **nuclear reactor control rods**.  
This helps **regulate fission reactions and prevent meltdowns**, ensuring nuclear reactors operate safely.
""")

# 🧴 Detergents & Bleaches
st.image("https://upload.wikimedia.org/wikipedia/commons/9/93/Washing_Powder.jpg", caption="Boron in Detergents", use_container_width=True)
st.markdown("""
### **🧴 Detergents & Bleaches**
Boron-based compounds like **sodium perborate** act as **oxidizing agents** in **detergents and bleaches**.  
They help in **removing stains, brightening clothes, and preventing bacterial growth**.  
Due to environmental concerns, some countries have regulated the use of **borate detergents**, encouraging alternatives.
""")

# 🌱 Agriculture
st.image("https://upload.wikimedia.org/wikipedia/commons/7/72/Boron_deficiency_in_plants.jpg", caption="Boron Deficiency in Plants", use_container_width=True)
st.markdown("""
### **🌱 Agriculture**
Boron is an **essential micronutrient for plants**, playing a crucial role in **cell wall formation, pollination, and nutrient transport**.  
A deficiency in boron leads to **stunted growth, poor root development, and reduced crop yields**.  
However, excessive boron can be toxic, causing **leaf burn and reduced plant productivity**.  
Farmers carefully manage boron levels in **soil and fertilizers** to optimize plant health.
""")

# 💻 Electronics
st.image("https://upload.wikimedia.org/wikipedia/commons/3/3e/Semiconductor_wafer.jpg", caption="Boron in Semiconductors", use_container_width=True)
st.markdown("""
### **💻 Electronics**
Boron is widely used in the **semiconductor industry**, especially for **doping silicon** to create **p-type semiconductors**.  
These semiconductors are used in **transistors, microchips, and solar panels**, improving the efficiency of modern electronics.  
Boron-based **nanomaterials** are also being explored for **next-generation computing and battery technologies**.
""")

st.divider()

# 🏥 Biological Importance
st.subheader("🏥 Biological Importance of Boron")
st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/Healthy_Fruits_and_Vegetables.jpg", caption="Boron in Diet", use_container_width=True)
st.write("""
Boron is **not classified as an essential element for humans**, but research suggests it plays a **significant role in bone health, brain function, and metabolism**.

### **🦴 Bone and Joint Health**
- Boron aids in **calcium absorption**, reducing the risk of **osteoporosis and arthritis**.  
- It helps in the **production of vitamin D**, crucial for bone strength.

### **🧠 Cognitive Function**
- Some studies indicate that boron **enhances memory, coordination, and cognitive performance**.  
- A deficiency may lead to **poor attention and slower reaction times**.

### **🍏 Dietary Sources of Boron**
- **Fruits** (apples, oranges, grapes)  
- **Nuts** (almonds, walnuts)  
- **Vegetables** (broccoli, spinach, carrots)  

Although boron is available in various foods, **supplements are sometimes recommended** for individuals at risk of deficiency.
""")

st.caption("References: [RSC - Boron](https://periodic-table.rsc.org/element/5/boron), [NIST Chemistry WebBook](https://webbook.nist.gov/)")

st.divider()

