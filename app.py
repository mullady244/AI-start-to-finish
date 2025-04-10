
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test 50", layout="centered")

st.title("Algebra Map – Version: Test 50")

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
# 🎯 OBJECTIVES – Categorize the Objectives (Dropdown View)
# -----------------------------
st.subheader("🎯 Objective Categorization")
st.markdown("Place each objective under its correct category. All categories contain valid objectives, but some options do NOT belong.")

# ✅ Define correct objectives grouped by category
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

# 🚫 Rotating incorrect objectives
rotating_incorrect_pool = [
    "Find the area of a circle",
    "Factor a trinomial",
    "Simplify a radical",
    "Determine triangle similarity",
    "Calculate the volume of a cone",
    "Identify asymptotes of a rational function"
]

# 📦 Initialize shuffled pool (once per session)
if "dropdown_objectives_pool" not in st.session_state:
    random.seed(st.session_state.get("seed_dropdown", random.randint(0, 999999)))
    incorrect_objectives = random.sample(rotating_incorrect_pool, 3)
    correct_objectives = [item for sublist in grouped_correct_objectives.values() for item in sublist]
    st.session_state.dropdown_objectives_pool = sorted(correct_objectives + incorrect_objectives)
    st.session_state.dropdown_feedback = {cat: [] for cat in grouped_correct_objectives}
    st.session_state.dropdown_selections = {cat: [] for cat in grouped_correct_objectives}

# 🔁 Redefine correct/incorrect every load
correct_objectives = [item for sublist in grouped_correct_objectives.values() for item in sublist]
incorrect_objectives = [obj for obj in st.session_state.dropdown_objectives_pool if obj not in correct_objectives]

# 🧠 Dropdowns and feedback
for category, valid_items in grouped_correct_objectives.items():
    st.markdown(f"### {category}")
    key = f"dropdown_{category}"

    # Feedback appears BEFORE dropdown
    for msg in st.session_state.dropdown_feedback[category]:
        if msg["type"] == "success":
            st.success(msg["text"])
        elif msg["type"] == "warning":
            st.warning(msg["text"])
        elif msg["type"] == "error":
            st.error(msg["text"])

    selected = st.multiselect(
        f"Select objectives for {category}:",
        options=st.session_state.dropdown_objectives_pool,
        default=st.session_state.dropdown_selections[category],
        key=key
    )

    # Only update state if changed
    if selected != st.session_state.dropdown_selections[category]:
        st.session_state.dropdown_selections[category] = selected
        new_feedback = []
        for obj in selected:
            if obj in valid_items:
                new_feedback.append({"type": "success", "text": f"{obj} ✔️ Correct"})
            elif obj in correct_objectives:
                new_feedback.append({"type": "warning", "text": f"{obj} ⚠️ Valid but belongs to another category"})
            else:
                new_feedback.append({"type": "error", "text": f"{obj} ❌ Not a valid linear equation objective"})
        st.session_state.dropdown_feedback[category] = new_feedback

# ✅ Final "I'm Done" button
st.markdown("---")
if st.button("✅ I'm Done"):
    st.success("🎉 Great job categorizing objectives! Let's move to the next step.")
    st.session_state.show_next_section = True

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
