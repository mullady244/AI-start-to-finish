
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test 22", layout="centered")

st.title("📘 Algebra Map – Version: Test 22")
st.header("🔢 Linear Equation Flow")

st.markdown("""
This is a conceptual exploration, not a solving practice space. Here we explain how to solve, not solve it for you.

💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.
""")

# Type Identification Section
st.subheader("🔍 Type Identification")
st.latex("3x + 5 = 14")
st.markdown("The equation above is a Linear Equation.")

tf_choice = st.radio("True or False?", options=["", "True", "False"], index=0)

# Objective Identification Section
st.subheader("🎯 Objective Identification")

all_options = ['Model real-world scenarios', 'Solve for x', 'Create a table of values', 'Find intersection of two lines', 'Convert to point-slope form', 'Identify slope and intercepts', 'Convert to slope-intercept form', 'Translate verbal → symbolic', 'Compare slopes of two lines', 'Convert to standard form', 'Determine if lines are parallel, perpendicular, or neither', 'Differentiate with respect to x', 'Simplify trigonometric expressions', 'Verify solution', 'Find the domain of a radical function', 'Find x- and y-intercepts', 'Translate symbolic → verbal', 'Graph the equation', 'Write the equation from two points', 'Describe the rate of change']
default_checked = ['Model real-world scenarios', 'Solve for x', 'Create a table of values', 'Find intersection of two lines', 'Convert to point-slope form', 'Identify slope and intercepts', 'Convert to slope-intercept form', 'Translate verbal → symbolic', 'Compare slopes of two lines', 'Convert to standard form', 'Determine if lines are parallel, perpendicular, or neither', 'Verify solution', 'Find x- and y-intercepts', 'Translate symbolic → verbal', 'Graph the equation', 'Write the equation from two points', 'Describe the rate of change']

user_selection = st.multiselect(
    "Uncheck incorrect objectives. Leave all correct ones checked.",
    options=all_options,
    default=default_checked
)

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
