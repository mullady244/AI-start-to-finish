
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test XVI", layout="wide")

st.title("📘 Algebra Map – Version: Test XVI")

# True/False Section
st.header("🔢 Linear Equation Flow")
st.latex("3x + 5 = 14")

st.markdown("**The following is a Linear Equation.**")
tf_answer = st.radio("Select True or False:", ["True", "False"], index=None)

if tf_answer is not None:
    if tf_answer == "True":
        st.success("✅ Correct! This is a linear equation.")
    else:
        st.error("❌ Incorrect. This is a linear equation because the variable is raised only to the first power and the graph is a straight line.")

# Objective Checkbox Section
st.markdown("---")
st.subheader("🎯 Linear Equations – What are the potential objectives/instructions?")
st.markdown("Uncheck the **incorrect** objectives. Leave all correct ones checked.")

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
    "Factor a quadratic",
    "Use the quadratic formula",
    "Simplify a rational expression",
    "Graph a parabola",
    "Find domain of a rational function",
    "Evaluate a logarithmic expression"
]

# Shuffle only once per session
if "shuffled_invalids" not in st.session_state:
    st.session_state.shuffled_invalids = random.sample(invalid_objectives_pool, 3)

display_objectives = valid_objectives + st.session_state.shuffled_invalids
random.shuffle(display_objectives)

checked_status = {obj: st.checkbox(obj, value=True) for obj in display_objectives}

# Validation
if st.button("Check Your Answers"):
    incorrect_checked = [obj for obj in st.session_state.shuffled_invalids if checked_status.get(obj)]
    correct_unchecked = [obj for obj in valid_objectives if not checked_status.get(obj)]
    
    if not incorrect_checked and not correct_unchecked:
        st.success("✅ Well done! You've correctly identified all relevant objectives.")
    else:
        if incorrect_checked:
            st.error(f"❌ The following are **not** valid objectives for linear equations: {', '.join(incorrect_checked)}")
        if correct_unchecked:
            st.error(f"⚠️ You mistakenly **unchecked** valid objectives: {', '.join(correct_unchecked)}")

# Footer with timestamp
st.markdown("---")
st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
