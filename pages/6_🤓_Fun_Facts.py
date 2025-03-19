import streamlit as st

st.set_page_config(
    page_title="Fun Facts",
    page_icon="🤓",
)
a = st.radio(
    "Choose an element to explore:",
    [":red[B]  🔥 Boron", ":violet[K]  ✨ Potassium",  ":orange[Kr] 🍀 Krypton"],
    index=None)
if a == ":red[B]  🔥 Boron":
    st.title("🧪 Mind-Blowing Facts About Boron")
    st.divider()
    
    # Facts list
    facts = [
        "💎 **Boron Can Make Fake Diamonds! 💠** - When combined with carbon under high pressure, boron forms **boron carbide**, which is nearly as hard as diamonds!",
        "🔥 **Boron Burns Green in Fireworks 🎆** - Fireworks and flares use **boron compounds** to create **bright green flames**!",
        "🚀 **Boron is Used in Rocket Fuel!** - Boron-based fuels, like **boranes**, have been tested for use in **high-energy rocket propellants**.",
        "💊 **Boron Keeps Your Bones Strong 🦴** - This element helps regulate **calcium and magnesium** in your body, making it crucial for **bone health**.",
        "🔫 **Used in Bulletproof Vests and Tank Armor 🛡️** - **Boron carbide** is one of the hardest materials known, making it perfect for **bulletproof vests** and **military armor**.",
        "💥 **Boron Can Absorb Radiation ☢️** - The nuclear industry uses **boron** to **absorb neutrons**, preventing dangerous chain reactions!",
        "🌱 **Essential for Plant Growth 🌿** - Without boron, plants wouldn’t be able to **grow properly**, as it’s essential for **cell wall formation**.",
        "🚰 **Boron Helps Purify Water 💧** - **Boron compounds** are used in **water filtration systems** to remove heavy metals and contaminants.",
        "🦠 **Boron May Have Helped Life Begin on Earth 🌍** - Some scientists believe that boron compounds played a role in **RNA formation**, which led to the origin of life!",
        "⚛️ **Boron Defies the Rules of Chemistry** - Unlike most elements, **boron forms unique electron-deficient bonds**, making its chemistry fascinatingly weird!",
        "💡 **Boron Makes Glass Stronger 🏗️** - **Borosilicate glass** (like Pyrex) is heat-resistant and used in **lab equipment, cookware, and telescopes**.",
        "🧠 **Boron Could Boost Your Brainpower 🧠⚡** - Studies suggest **boron improves memory and focus**, making it important for brain health!",
    ]
    
    # Display facts
    for fact in facts:
        st.markdown(fact)
        st.divider()

elif a == ":violet[K]  ✨ Potassium" :
    

    # Title
    st.title("🔥Mind-Blowing Facts About Potassium ⚡")
    st.divider()
    # Facts list
    facts = [
        "🍌 **Bananas Are *Technically* Radioactive ☢️** - Bananas contain Potassium-40, a naturally radioactive isotope. You'd need to eat **10 million bananas** at once to get a lethal dose of radiation!",
        "In the early 19th century, scientists initially believed potassium and sodium were the same element due to their similar properties—until Davy’s electrolysis experiments proved otherwise.",
        "Potassium nitrate (saltpeter) was a key ingredient in gunpowder, used in warfare since at least the 9th century by the Chinese and later in European cannons.",
        "Potassium chlorate (KClO₃) was a key ingredient in early chemical warfare, used in explosives and poison gas production.",
        "Used in spy suicides, assassinations, and executions, potassium cyanide (KCN) was historically a deadly poison used by figures like Nazi leaders, Cold War spies, and political prisoners.",
        "🩸 **Potassium in Your Blood Could Kill You (If It Leaks) ⚠️** - If too much potassium leaks into your bloodstream (**hyperkalemia**), it can **stop your heart** almost instantly.",
        "🧠 **Your Brain Runs on Potassium ⚡** - Neurons use potassium to send **electrical signals** throughout your body. Without it, your muscles wouldn’t move, and your brain couldn’t think!",
        "🔥 **Potassium Burns with a *Purple-Pink* Flame 💜** - If you set potassium metal on fire, it produces a **stunning lilac flame**—used in flame tests to identify it.",
        "💥 **More Explosive Than Sodium in Water 🌊** - Potassium reacts **violently** with water, **exploding instantly** due to rapid hydrogen gas production!",
        "🏋️‍♂️ **Your Body Has About 120g of Potassium** - The human body contains around **120g of potassium**, enough to **make a tiny bomb** if purified!",
        "🦴 **Potassium Salts Can Be Used to 'Disappear' Bodies** - Potassium hydroxide is used in **alkaline hydrolysis**, a method that dissolves human remains into liquid in **a few hours**.",
        "🌱 **Plants Love Potassium More Than We Do 💚** - Potassium helps plants **move water, resist diseases, and produce sugars**. Without potassium fertilizers, **crop production would drop drastically**.",
        "🌍 **Potassium-40 Keeps Earth Warm 🔥** - Potassium-40 contributes to **Earth’s internal heat**, as its **radioactive decay** powers geothermal energy inside the planet.",
        "⚡❤️ **Too Much Potassium Can Stop Your Heart Instantly** - **Lethal injections** use **potassium chloride** to stop the heart in seconds by preventing muscle contraction."
    ]
    
    # Display facts
    for fact in facts:
        st.markdown(fact)
        st.divider()

elif a == ":orange[Kr] 🍀 Krypton" :
   # Title
    st.title("💡 Mind-Blowing Facts About Krypton 🔥")  
    st.divider()  
    
    # Facts list
    facts = [
        "💨 **Krypton Is a Ghostly Noble Gas 👻** - This colorless, odorless gas got its name from the Greek word *kryptos*, meaning 'hidden'—fitting for an element that’s hard to find!",
        "🦸‍♂️ **Not Just Superman's Home Planet! 🌍** - Despite its name, krypton has no connection to Kryptonite—the famous fictional mineral that weakens Superman.",
        "💡 **Krypton Glows Bright in Neon Lights! 🔥** - While krypton itself is invisible, in gas discharge tubes, it emits a beautiful **white-blue glow**, used in specialty lighting.",
        "🧊 **Colder Than Antarctica ❄️** - Liquid krypton forms at **-153°C (-243°F)**, making it much colder than Earth's coldest temperatures!",
        "⚡ **Used in High-Powered Lasers 🔥** - Krypton fluoride (KrF) is used in **powerful excimer lasers**, essential for eye surgery and semiconductor manufacturing.",
        "🚀 **Krypton Can Power Spacecraft! 🚀** - NASA has used krypton gas as a **propellant** in ion thrusters, an advanced technology for deep-space missions.",
        "🌌 **There’s Krypton in the Air You Breathe! 🌍** - Krypton makes up **0.0001%** of Earth’s atmosphere, meaning every breath you take contains tiny traces of it.",
        "🎥 **Hollywood Uses Krypton for Cinematic Effects 🎬** - Some high-intensity flash lamps in photography and film lighting contain krypton gas to create ultra-bright flashes.",
        "💀 **Krypton Gas Can Knock You Out ☠️** - In high concentrations, krypton acts as a **narcotic anesthetic**, potentially leading to unconsciousness!",
        "⚛️ **Krypton Is Used to Detect Nuclear Bomb Tests ☢️** - Krypton-85, a radioactive isotope, is released during nuclear fission, helping scientists track secret nuclear tests worldwide.",
    ]
    
    # Display facts
    for fact in facts:
        st.markdown(fact)
        st.divider()
