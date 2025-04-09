
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test 24", layout="centered")

st.title("Algebra Map – Version: Test 24")

st.markdown("This is a conceptual exploration, not a solving practice space. Here we explain how to solve, not solve it for you.")
st.markdown("💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.")

# -----------------------------
# 🔍 TYPE IDENTIFICATION
# -----------------------------
st.subheader("🔍 Type Identification")

equation = "3x + 5 = 14"
st.latex(equation)
st.markdown("**The equation above is a Linear Equation.**")

type_response = st.radio("True or False?", options=["", "True", "False"], index=0)

if type_response:
    if type_response == "True":
        st.success("✅ Correct! This is a linear equation.")
    else:
        st.error("❌ Incorrect. This is indeed a linear equation.")

# -----------------------------
# 🎯 OBJECTIVES – Trim the Incorrect
# -----------------------------
st.subheader("🎯 Objectives for Linear Equations")
st.markdown("Uncheck the incorrect objectives. Leave all correct ones checked.")

correct_objectives = [
    "Solve for x",
    "Graph the equation",
    "Convert to standard form",
    "Convert to slope-intercept form",
    "Convert to point-slope form",
    "Find x- and y-intercepts",
    "Identify slope and intercepts",
    "Compare slopes of two lines",
    "Determine if lines are parallel, perpendicular, or neither",
    "Find intersection of two lines",
    "Verify solution",
    "Model real-world scenarios",
    "Translate verbal → symbolic",
    "Translate symbolic → verbal",
    "Describe the rate of change",
    "Write the equation from two points"
]

rotating_incorrect_pool = [
    "Find the area of a circle",
    "Factor a trinomial",
    "Simplify a radical",
    "Determine triangle similarity",
    "Calculate the volume of a cone",
    "Identify asymptotes of a rational function"
]

random.seed(st.session_state.get("seed_obj", random.randint(0, 999999)))
if "seed_obj" not in st.session_state:
    st.session_state["seed_obj"] = random.randint(0, 999999)
incorrect_objectives = random.sample(rotating_incorrect_pool, 3)

all_objectives = correct_objectives + incorrect_objectives
random.shuffle(all_objectives)

if "objective_states" not in st.session_state:
    st.session_state.objective_states = {obj: True for obj in all_objectives}

incorrect_unchecked = []
correct_unchecked = []

for obj in all_objectives:
    current_state = st.checkbox(obj, value=st.session_state.objective_states.get(obj, True), key=obj)
    st.session_state.objective_states[obj] = current_state

    if obj in correct_objectives and not current_state:
        correct_unchecked.append(obj)
    if obj in incorrect_objectives and not current_state:
        incorrect_unchecked.append(obj)

if correct_unchecked:
    st.error("❌ You unchecked one or more correct objectives. Review and try again.")
elif len(incorrect_unchecked) == len(incorrect_objectives):
    st.success("✅ Well done! You correctly identified all the valid objectives.")

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
