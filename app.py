
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test 41", layout="centered")

st.title("Algebra Map – Version: Test 41")

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

# 🔁 Pick 3 fake objectives randomly (once per session)
if "seed_obj" not in st.session_state:
    st.session_state["seed_obj"] = random.randint(0, 999999)
random.seed(st.session_state["seed_obj"])
incorrect_objectives = random.sample(rotating_incorrect_pool, 3)

# 📦 Flatten correct objectives and combine
correct_objectives = [item for sublist in grouped_correct_objectives.values() for item in sublist]
all_objectives = correct_objectives + incorrect_objectives

# 🧾 Initialize checkbox states ONCE per session
if "objectives_initialized" not in st.session_state:
    st.session_state.objective_states = {
        obj: True for obj in all_objectives  # ✅ All boxes start checked
    }
    st.session_state.objectives_initialized = True

# ✅ Map incorrect objectives into 3 random categories
category_names = list(grouped_correct_objectives.keys())
random_categories = random.sample(category_names, 3)
injected_incorrects = dict(zip(random_categories, incorrect_objectives))

# ✅ Show all objectives grouped — injecting fake ones
if "last_changed_obj" not in st.session_state:
    st.session_state["last_changed_obj"] = None

for category, items in grouped_correct_objectives.items():
    with st.expander(category, expanded=True):
        combined_items = items + ([injected_incorrects[category]] if category in injected_incorrects else [])
        for obj in combined_items:
            prev = st.session_state.objective_states.get(obj, True)
            current_state = st.checkbox(obj, value=prev, key=obj)

            if current_state != prev:
                st.session_state["last_changed_obj"] = obj

            st.session_state.objective_states[obj] = current_state

            # 🔁 Inline feedback directly under the item that was just changed
if st.session_state["last_changed_obj"] == obj:
    if obj in correct_objectives and not current_state:
        st.error("❌ This is a valid objective.")
    elif obj in incorrect_objectives and not current_state:
        unchecked_count = sum(
            not st.session_state.objective_states.get(inc, True) 
            for inc in incorrect_objectives
        )
        if unchecked_count == len(incorrect_objectives):
            st.success("✅ You are complete. All incorrect objectives removed.")
        else:
            st.success("✅ Correct. This is not a valid objective.")

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
