
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test 46", layout="centered")

st.title("Algebra Map – Version: Test 46")

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

# 🚫 Define distractors
rotating_incorrect_pool = [
    "Find the area of a circle",
    "Factor a trinomial",
    "Simplify a radical",
    "Determine triangle similarity",
    "Calculate the volume of a cone",
    "Identify asymptotes of a rational function"
]

# 🎯 Prepare objectives (3 distractors per session)
if "dropdown_objectives_pool" not in st.session_state:
    random.seed(st.session_state.get("seed_dropdown", random.randint(0, 999999)))
    incorrect_objectives = random.sample(rotating_incorrect_pool, 3)
    correct_objectives = [item for sublist in grouped_correct_objectives.values() for item in sublist]
    st.session_state.dropdown_objectives_pool = sorted(correct_objectives + incorrect_objectives)

# 🎯 Track correct and incorrect
correct_objectives = [item for sublist in grouped_correct_objectives.values() for item in sublist]
incorrect_objectives = [obj for obj in st.session_state.dropdown_objectives_pool if obj not in correct_objectives]

# 🧠 Track selections by category
if "dropdown_selections" not in st.session_state:
    st.session_state.dropdown_selections = {category: [] for category in grouped_correct_objectives.keys()}

# 🎯 Generate dropdowns and show feedback
for category, valid_items in grouped_correct_objectives.items():
    st.markdown(f"### {category}")
    key = f"dropdown_{category}"
    
    selected = st.multiselect(
        f"Select objectives for {category}:",
        options=st.session_state.dropdown_objectives_pool,
        default=st.session_state.dropdown_selections.get(category, []),
        key=key
    )
    
    st.session_state.dropdown_selections[category] = selected

    for obj in selected:
        if obj in valid_items:
            st.success(f"✅ {obj} is correct for this category.")
        elif obj in correct_objectives:
            st.warning(f"⚠️ {obj} is valid but belongs to a different category.")
        else:
            st.error(f"❌ {obj} is not a valid objective for linear equations.")

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
