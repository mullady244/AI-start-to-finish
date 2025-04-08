
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test XVII", layout="wide")
st.title("📘 Algebra Map – Version: Test XVII")

st.markdown("### 🔢 Linear Equation Flow")
st.latex("3x + 5 = 14")
st.markdown("This is a conceptual exploration, not a solving practice space. Here we explain how to solve, not solve it for you.")
st.markdown("💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.")

st.markdown("---")
st.subheader("🔍 Type Identification")
st.markdown("**The following is a Linear Equation.**")
tf_answer = st.radio("True or False?", ["True", "False"], key="tf_q1")

if tf_answer:
    if tf_answer == "True":
        st.success("✅ Correct! This is a linear equation.")
    else:
        st.error("❌ Incorrect. A linear equation has variables raised to the power of 1, like 3x + 5 = 14.")

st.markdown("---")
st.subheader("🎯 Objective Recognition")

valid_objectives = [
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

invalid_objectives_pool = [
    "Factor a trinomial",
    "Simplify a rational expression",
    "Evaluate a logarithmic function",
    "Find the domain of a radical function",
    "Graph a sine wave",
    "Use the quadratic formula",
    "Determine end behavior of a polynomial"
]

if "objective_options" not in st.session_state:
    random_invalids = random.sample(invalid_objectives_pool, 3)
    all_options = valid_objectives + random_invalids
    random.shuffle(all_options)
    st.session_state.objective_options = all_options
    st.session_state.correct_set = set(valid_objectives)
    st.session_state.incorrect_set = set(random_invalids)

st.markdown("**Uncheck incorrect objectives. Leave all correct ones checked.**")

incorrect_unchecked = []
correct_unchecked = []

for obj in st.session_state.objective_options:
    key = f"cb_{obj}"
    current_state = st.checkbox(obj, value=True, key=key)
    if not current_state:
        if obj in st.session_state.correct_set:
            correct_unchecked.append(obj)
        elif obj in st.session_state.incorrect_set:
            incorrect_unchecked.append(obj)

if correct_unchecked:
    st.error(f"⚠️ Oops! You incorrectly unchecked a valid objective: {', '.join(correct_unchecked)}")
elif len(incorrect_unchecked) == len(st.session_state.incorrect_set):
    st.success("🎉 Well done! You correctly trimmed all incorrect objectives.")

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
