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
    st.write("Write here")

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
    st.title("💡 The Hidden Wonders of Krypton ")  
    st.subheader("A Noble Gas with Superpowers!")  
    st.divider()  
    
    # Fact 1: The Name's Meaning  
    st.subheader("🔎 **Krypton Means 'Hidden'!**")  
    st.markdown("This noble gas gets its name from the Greek word **'kryptos'**, meaning **'hidden'**—a perfect fit for an element that's rare and elusive!")  
    st.divider()  
    
    # Fact 2: Not Just Superman’s Home!  
    st.subheader("🦸‍♂️ **Krypton ≠ Kryptonite!**")  
    st.markdown("Despite its sci-fi fame, **krypton is NOT related to Kryptonite**. But hey, if Superman ever needs some cool glow-in-the-dark lighting, krypton gas has his back!")  
    st.divider()  
    
    # Fact 3: Krypton Lights Up the World  
    st.subheader("💡 **Krypton Creates a Stunning White-Blue Glow**")  
    st.markdown("Though krypton is **invisible**, when used in gas discharge tubes, it produces a **brilliant white-blue light**, perfect for neon signs and airport runway lights.")  
    st.divider()  
    
    # Fact 4: Super Cold Liquid  
    st.subheader("❄️ **Colder Than Antarctica!**")  
    st.markdown("Krypton turns into a liquid at **-153°C (-243°F)**—way colder than Earth’s iciest places! If you had a glass of liquid krypton, it’d freeze your hand instantly.")  
    st.divider()  
    
    # Fact 5: Space Propulsion Power  
    st.subheader("🚀 **Fuel for the Future? Krypton in Space!**")  
    st.markdown("NASA has experimented with krypton gas as a **propellant** in ion thrusters, helping satellites and spacecraft travel through space efficiently.")  
    st.divider()  
    
    # Fact 6: There’s Krypton in Your Breath!  
    st.subheader("🌍 **You Breathe Krypton Every Day!**")  
    st.markdown("Krypton makes up **0.0001%** of Earth’s atmosphere. That means **every breath you take contains traces of krypton!**")  
    st.divider()  
    
    # Fact 7: The Science Behind Nuclear Detection  
    st.subheader("☢️ **Spies Use Krypton to Track Nukes!**")  
    st.markdown("The isotope **Krypton-85** is released in nuclear explosions, allowing scientists and intelligence agencies to detect **secret nuclear tests** worldwide.")  
    st.divider()  
    
    # Fact 8: Krypton’s Hidden Danger  
    st.subheader("💀 **Too Much Krypton = Instant Nap!**")  
    st.markdown("At high concentrations, krypton acts as a **narcotic anesthetic**, meaning it can knock you out—just like **laughing gas, but without the giggles!**")  
    st.divider()  
    
    # Fact 9: Hollywood Uses Krypton!  
    st.subheader("🎥 **Krypton in the Movies!**")  
    st.markdown("High-intensity flash lamps in photography and movie productions use krypton gas to create **ultra-bright light bursts** for stunning cinematic effects.")  
    st.divider()  
    
    # Fact 10: The Coolest Sci-Fi Element  
    st.subheader("🌌 **Krypton: The Most Sci-Fi Element?**")  
    st.markdown("From being Superman’s home planet to powering **futuristic lasers**, krypton is **the most sci-fi-sounding element on the periodic table!**")  
    st.divider()
