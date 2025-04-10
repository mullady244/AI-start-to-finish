
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test 43", layout="centered")

st.title("Algebra Map – Version: Test 43")

st.markdown("This is a conceptual exploration, not a solving practice space. Here we explain how to solve, not solve it for you.")
st.markdown("💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.")

# -----------------------------
# 🔍 TYPE IDENTIFICATION
# -----------------------------
st.subheader("🔍 Type Identification")

equation = "3x + 5 = 14"
st.latex(equation)
st.markdown("**The equation above is a Linear Equation.**")

type_response = st.radio("True or False?", options=["True", "False"], index=None)

if type_response:
    if type_response == "True":
        st.success("✅ Correct! This is a linear equation.")
    else:
        st.error("❌ Incorrect. This is indeed a linear equation.")

# -----------------------------
# 🎯 OBJECTIVES – Categorize the Objectives (Dropdown Assignment)
# -----------------------------
st.subheader("🎯 Objectives for Linear Equations")
st.markdown("Assign the correct objectives to each category using the dropdown menu. Some items do not belong in any category — leave them unassigned.")

# ✅ Define grouped correct objectives by category
grouped_correct_objectives = {
    "🔢 Algebraic Manipulation": ["Solve for x"],
    "🔁 Form Conversion": [
        "Convert to standard form",
        "Convert to slope-intercept form",
        "Convert to point-slope form"
    ],
    "📊 Visual Representation": [
        "Graph the equation",
        "Create a table of values"
    ],
    "📍 Feature Extraction": [
        "Find x- and y-intercepts",
        "Identify slope and intercepts"
    ],
    "🔍 Conceptual Comparison": [
        "Compare slopes of two lines",
        "Determine if lines are parallel, perpendicular, or neither"
    ],
    "➕ System Relationships": ["Find intersection of two lines"],
    "🧠 Reasoning": ["Verify solution"],
    "🌍 Real-World Modeling": ["Model real-world scenarios"],
    "🔤 Language Link": [
        "Translate verbal → symbolic",
        "Translate symbolic → verbal"
    ],
    "📈 Rate Understanding": ["Describe the rate of change"],
    "✍️ Equation Creation": ["Write the equation from two points"]
}

# 🚫 Rotating incorrect distractors (some realistic, some clearly wrong)
rotating_incorrect_pool = [
    "Factor a trinomial",
    "Calculate the volume of a cone",
    "Simplify a radical",
    "Find the area of a circle",
    "Identify asymptotes of a rational function",
    "Determine triangle similarity",
    "Find the domain of a function",
    "Use quadratic formula",
]

# 🔁 Randomize distractors (5)
if "seed_dropdown" not in st.session_state:
    st.session_state["seed_dropdown"] = random.randint(0, 999999)
random.seed(st.session_state["seed_dropdown"])
distractors = random.sample(rotating_incorrect_pool, 5)

# 📦 Build full list of shuffled options
all_true_objectives = [item for sublist in grouped_correct_objectives.values() for item in sublist]
all_dropdown_options = all_true_objectives + distractors
random.shuffle(all_dropdown_options)

# 🧠 Store user picks by category
if "dropdown_selections" not in st.session_state:
    st.session_state.dropdown_selections = {}

# 🔽 Create a dropdown per category
for category in grouped_correct_objectives.keys():
    selection = st.multiselect(
        f"{category}:",
        options=all_dropdown_options,
        default=st.session_state.dropdown_selections.get(category, []),
        key=f"dropdown_{category}"
    )
    st.session_state.dropdown_selections[category] = selection

    # 👁️ Show full selections below to avoid truncation
    if selection:
        st.markdown("✅ You selected:")
        for obj in selection:
            st.markdown(f"- {obj}")

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
