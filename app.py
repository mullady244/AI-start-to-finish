
import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="Algebra Map – Version: Test 23", layout="wide")

st.title("📘 Algebra Map – Version: Test 23")
st.header("🔢 Linear Equation Flow")

st.markdown("This is a conceptual exploration, not a solving practice space. Here we explain how to solve, not solve it for you.")
st.info("💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.")

# Type Identification Section
st.subheader("🔍 Type Identification")
st.latex("3x + 5 = 14")
st.write("The equation above is a Linear Equation.")

type_tf = st.radio("True or False?", options=["", "True", "False"], index=0)

if type_tf:
    if type_tf == "True":
        st.success("✅ Correct! This is a linear equation.")
    else:
        st.error("❌ Incorrect. A linear equation is an equation of the form ax + b = c.")

# Objective Identification
st.subheader("🎯 Objective Identification")

all_objectives = [
    "Solve for x",
    "Graph the equation",
    "Convert to standard form",
    "Convert to slope-intercept form",
    "Convert to point-slope form",
    "Create a table of values",
    "Find x- and y-intercepts",
    "Identify slope and intercepts",
    "Compare slopes of two lines",
    "Determine if lines are parallel or perpendicular or neither",
    "Find intersection of two lines",
    "Verify solution",
    "Model real-world scenarios",
    "Translate verbal → symbolic",
    "Translate symbolic → verbal",
    "Describe the rate of change",
    "Write the equation from two points"
]

incorrect_objectives_pool = [
    "Find the area of a circle",
    "Factor a quadratic expression",
    "Determine the domain of a rational function",
    "Simplify a trigonometric identity",
    "Solve a logarithmic inequality"
]

random.seed(42)
wrong_choices = random.sample(incorrect_objectives_pool, 3)
objectives_mixed = all_objectives + wrong_choices

initial_states = {obj: True for obj in objectives_mixed}
selected = st.multiselect(
    "Uncheck incorrect objectives. Leave all correct ones checked.",
    options=objectives_mixed,
    default=list(initial_states.keys())
)

# Evaluation
wrong_unchecked = [w for w in wrong_choices if w not in selected]
correct_unchecked = [o for o in all_objectives if o not in selected]

if correct_unchecked:
    st.warning("⚠️ You unchecked valid objectives. Re-check them to proceed confidently.")
elif len(wrong_unchecked) == len(wrong_choices):
    st.success("✅ Excellent! All incorrect objectives have been successfully removed.")

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
