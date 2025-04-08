
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test XVIII", layout="wide")

# --- HEADER ---
st.title("📘 Algebra Map – Version: Test XVIII")
st.header("🔢 Linear Equation Flow")

st.latex("3x + 5 = 14")
st.markdown("This is a conceptual exploration, not a solving practice space. Here we explain how to solve, not solve it for you.")
st.markdown("💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.")

# --- TYPE IDENTIFICATION ---
st.subheader("🔍 Type Identification")
st.markdown("The equation above is a Linear Equation.")
tf_response = st.radio("True or False?", ["True", "False"])

if tf_response:
    if tf_response == "True":
        st.success("✅ Correct! This is a linear equation.")
    else:
        st.error("❌ Incorrect. A linear equation has the variable to the first power and graphs a straight line.")

# --- OBJECTIVES CHECKBOX CHALLENGE ---
st.subheader("🎯 Objective Recognition")

st.markdown("**Uncheck the incorrect objectives. Leave all correct ones checked.**")

correct_objectives = [
    "Solve for x",
    "Convert to standard form",
    "Convert to slope-intercept form",
    "Convert to point-slope form",
    "Graph the equation",
    "Create a table of values",
    "Find x- and y-intercepts",
    "Identify slope and intercepts",
    "Compare slopes of two lines",
    "Determine if lines are parallel or perpendicular",
    "Find intersection of two lines",
    "Verify solution",
    "Model real-world scenarios",
    "Translate verbal → symbolic",
    "Translate symbolic → verbal",
    "Describe the rate of change",
    "Write the equation from two points"
]

distractors_pool = [
    "Factor trinomials",
    "Simplify square roots",
    "Apply Pythagorean Theorem",
    "Find volume of a sphere",
    "Differentiate using chain rule",
    "Solve inequalities with absolute value",
    "Graph sine and cosine curves",
    "Integrate using substitution"
]

# Shuffle and limit distractors
random.seed(18)
distractors = random.sample(distractors_pool, 3)
all_objectives = correct_objectives + distractors
random.shuffle(all_objectives)

checked = {}
for obj in all_objectives:
    checked[obj] = st.checkbox(obj, value=True)

# Evaluate and give feedback
if st.button("Submit Objective Check"):
    incorrect_flags = []
    missed_flags = []

    for obj in all_objectives:
        if obj in correct_objectives and not checked[obj]:
            missed_flags.append(obj)
        elif obj not in correct_objectives and checked[obj]:
            incorrect_flags.append(obj)

    if not incorrect_flags and not missed_flags:
        st.success("✅ Perfect! All correct objectives kept, and incorrect ones removed.")
    else:
        if incorrect_flags:
            st.warning("⚠️ These were incorrect but left checked: " + ", ".join(incorrect_flags))
        if missed_flags:
            st.error("❌ These were correct but got unchecked: " + ", ".join(missed_flags))

# --- FOOTER TIMESTAMP ---
st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
