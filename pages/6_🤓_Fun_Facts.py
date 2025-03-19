import streamlit as st

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
