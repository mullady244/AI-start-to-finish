
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test 42", layout="centered")

st.title("Algebra Map – Version: Test 42")

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
# 🎯 OBJECTIVES – Categorize Each Objective (Dropdown View)
# -----------------------------
st.subheader("🎯 Objectives for Linear Equations")
st.markdown("Select all valid objectives under each category. Distractors may be hidden among the choices.")

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

# 🚫 Pool of incorrect (planted) distractors
rotating_incorrect_pool = [
    "Find the area of a circle",
    "Factor a trinomial",
    "Simplify a radical",
    "Determine triangle similarity",
    "Calculate the volume of a cone",
    "Identify asymptotes of a rational function"
]

# 🔁 Pick 3 incorrect objectives and randomly assign to categories
if "seed_obj" not in st.session_state:
    st.session_state["seed_obj"] = random.randint(0, 999999)
random.seed(st.session_state["seed_obj"])
incorrect_objectives = random.sample(rotating_incorrect_pool, 3)

category_names = list(grouped_correct_objectives.keys())
random_categories = random.sample(category_names, 3)
injected_incorrects = dict(zip(random_categories, incorrect_objectives))

# 🧠 Track performance
all_correct = True

# ✅ Show multiselect per category with feedback
for category, correct_items in grouped_correct_objectives.items():
    injected = [injected_incorrects[category]] if category in injected_incorrects else []
    all_options = correct_items + injected
    all_options.sort()  # Optional for cleaner display

    user_selection = st.multiselect(
        f"📂 {category}: Select all that apply",
        options=all_options,
        key=f"{category}_selection"
    )

    # 🧪 Check answers per category
    selected_set = set(user_selection)
    correct_set = set(correct_items)

    if selected_set:
        if selected_set == correct_set:
            st.success("✅ Correct! All valid objectives selected.")
        elif correct_set.issubset(selected_set):
            st.warning("⚠️ You selected too many. One or more choices are incorrect.")
            all_correct = False
        elif selected_set == correct_set - selected_set:
            st.warning("⚠️ Missing one or more correct objectives.")
            all_correct = False
        else:
            st.error("❌ Your selection has both missing and extra objectives.")
            all_correct = False
    else:
        all_correct = False

# ✅ Final message if all categories are correctly completed
if all_correct:
    st.success("🎉 All categories completed perfectly!")

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
