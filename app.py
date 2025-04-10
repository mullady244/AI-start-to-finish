
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test 44", layout="centered")

st.title("Algebra Map – Version: Test 44")

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
# 🎯 OBJECTIVES - Categorize by Dropdown with Feedback
# -----------------------------
st.subheader("🌟 Categorize the Objectives")
st.markdown("Select the appropriate objectives under each category. Some distractors are mixed in!")

# 🔢 Define grouped correct objectives by category
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
    "🌤️ Language Link": [
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

# ⟳ Sample 3 incorrect per session
if "shuffled_objectives" not in st.session_state:
    incorrect_objectives = random.sample(rotating_incorrect_pool, 3)
    correct_objectives = [item for sublist in grouped_correct_objectives.values() for item in sublist]
    st.session_state.shuffled_objectives = sorted(correct_objectives + incorrect_objectives)

# 🔢 Track correct and incorrect sets
correct_objectives = [item for sublist in grouped_correct_objectives.values() for item in sublist]
incorrect_objectives = [item for item in st.session_state.shuffled_objectives if item not in correct_objectives]

# 📝 Record user selections per category
if "category_selections" not in st.session_state:
    st.session_state.category_selections = {cat: [] for cat in grouped_correct_objectives.keys()}

# 🌟 Dropdown and feedback per category
for category, correct_items in grouped_correct_objectives.items():
    st.markdown(f"### {category}")
    options = st.multiselect(
        f"Select objectives for {category}:",
        options=st.session_state.shuffled_objectives,
        default=st.session_state.category_selections[category],
        key=f"select_{category}"
    )
    st.session_state.category_selections[category] = options

    # Feedback under dropdown
    for obj in options:
        if obj in correct_items:
            st.success(f"{obj} ✔️ Correct")
        elif obj in correct_objectives:
            st.warning(f"{obj} ⚠️ Correct for another category")
        else:
            st.error(f"{obj} ❌ Not a valid objective")

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
