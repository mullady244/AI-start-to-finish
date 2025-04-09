
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test 29", layout="centered")

st.title("Algebra Map – Version: Test 29")

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
# 🎯 OBJECTIVES – Trim the Incorrect (Grouped View)
# -----------------------------
st.subheader("🎯 Objectives for Linear Equations")
st.markdown("Uncheck the incorrect objectives. Leave all correct ones checked.")

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

# 🚫 Rotating incorrect (planted) distractors
rotating_incorrect_pool = [
    "Find the area of a circle",
    "Factor a trinomial",
    "Simplify a radical",
    "Determine triangle similarity",
    "Calculate the volume of a cone",
    "Identify asymptotes of a rational function"
]

# 🔁 Randomly pick 3 fake objectives
random.seed(st.session_state.get("seed_obj", random.randint(0, 999999)))
if "seed_obj" not in st.session_state:
    st.session_state["seed_obj"] = random.randint(0, 999999)
incorrect_objectives = random.sample(rotating_incorrect_pool, 3)

# 📦 Flatten correct objectives for logic handling
correct_objectives = [item for sublist in grouped_correct_objectives.values() for item in sublist]

# 🧠 Merge and track state
all_objectives = correct_objectives + incorrect_objectives
random.shuffle(all_objectives)

# 🧾 Initialize checkbox states
if "objective_states" not in st.session_state or set(st.session_state.objective_states.keys()) != set(all_objectives):
    st.session_state.objective_states = {
    obj: True if obj in correct_objectives else False
    for obj in all_objectives
}
# ✅ Group correct objectives AFTER all_objectives and session state setup
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

# ✅ Show checkboxes grouped by category
for category, items in grouped_correct_objectives.items():
    with st.expander(category, expanded=True):
        for obj in items:
            current_state = st.checkbox(obj, value=st.session_state.objective_states.get(obj, True), key=obj)
            st.session_state.objective_states[obj] = current_state

# 🚫 Show incorrect distractors under separate header
with st.expander("🚫 Not Linear Equation Objectives (planted distractions)", expanded=True):
    for obj in incorrect_objectives:
        current_state = st.checkbox(obj, value=st.session_state.objective_states.get(obj, True), key=obj)
        st.session_state.objective_states[obj] = current_state

# 🧠 Feedback logic
incorrect_unchecked = [obj for obj in incorrect_objectives if not st.session_state.objective_states.get(obj, True)]
correct_unchecked = [obj for obj in correct_objectives if not st.session_state.objective_states.get(obj, True)]

if correct_unchecked:
    st.error("❌ You unchecked one or more correct objectives. Review and try again.")
elif len(incorrect_unchecked) == len(incorrect_objectives):
    st.success("✅ Well done! You correctly identified all the valid objectives.")

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
