
import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="Algebra Map – Version: Test X", layout="centered")

# Header
st.title("📘 Algebra Map – Version: Test X")
st.success("✅ You’re viewing the latest version – Test X")
st.write("🔢 **Linear Equation Learning Flow**")
st.markdown("*This is a conceptual exploration space. We teach how to solve, but you solve in your notebook.*")
st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# -----------------------
# Step: Objective Evaluation (Uncheck Wrong)
# -----------------------

st.subheader("🎯 Step: What are the Objectives or Instructions for Linear Equations?")
st.write("All items are currently selected. Uncheck the ones that do **not** apply.")

# Valid objectives
valid_objectives = [
    "Solve for x",
    "Graph the equation",
    "Convert to standard form",
    "Write from two points",
    "Find intercepts",
    "Verify solution",
    "Model real-world scenarios"
]

# Distractors
distractor_pool = [
    "Factor the trinomial",
    "Find the vertex",
    "Simplify a radical expression",
    "Use the quadratic formula",
    "Identify the asymptotes",
    "Find the amplitude",
    "Determine end behavior",
    "Rewrite in vertex form"
]

# Shuffle on first session only
if "all_options" not in st.session_state:
    selected_distractors = random.sample(distractor_pool, 3)
    all_options = valid_objectives + selected_distractors
    random.shuffle(all_options)
    st.session_state.all_options = all_options
    st.session_state.feedback = {}

# Display all options with default checked
user_selection = {}
for option in st.session_state.all_options:
    user_selection[option] = st.checkbox(option, value=True, key=option)

# Evaluation button
if st.button("Check Your Selections"):
    wrong_unchecked = []
    correct_unchecked = []
    for option, is_checked in user_selection.items():
        if option in valid_objectives and not is_checked:
            correct_unchecked.append(option)
        elif option not in valid_objectives and is_checked:
            wrong_unchecked.append(option)

    if correct_unchecked:
        st.error("🚫 You unchecked one or more valid objectives:")
        for item in correct_unchecked:
            st.markdown(f"- ❗ `{item}` is an essential linear objective.")
    elif all(not user_selection[item] for item in st.session_state.all_options if item not in valid_objectives):
        st.success("🎉 Great job! You’ve correctly identified all valid objectives.")
    else:
        st.warning("🔎 You still have one or more incorrect items selected. Try again!")

# Reset button
if st.button("🔄 Reset"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()
