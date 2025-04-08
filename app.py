from datetime import datetime
import streamlit as st
import random

# --- PAGE SETUP ---
st.set_page_config(page_title="Algebra Map – Test XIII", layout="wide")
st.title("📘 Algebra Map – Version: Test XIII")
st.caption(f"🕒 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.markdown("---")

# --- SESSION STATE ---
if "checkbox_states" not in st.session_state:
    st.session_state.checkbox_states = {}
if "distractors_shuffled" not in st.session_state:
    st.session_state.distractors_shuffled = random.sample([
        "Find cube root", "Calculate standard deviation", "Plot sinusoidal curve",
        "Factor a trinomial", "Graph a logarithmic curve", "Use imaginary numbers"
    ], 3)
if "tf_response" not in st.session_state:
    st.session_state.tf_response = None
if "tf_feedback" not in st.session_state:
    st.session_state.tf_feedback = ""

# --- SECTION 1: T/F Type ID ---
def type_identification_step():
    st.subheader("🔍 Step 1: Type Identification")
    st.markdown("Is the following a **Linear Equation**?")
    st.latex("3x + 5 = 14")

    response = st.radio("True or False?", ["True", "False"], index=None, key="tf_radio")
    if st.button("Submit T/F Answer"):
        st.session_state.tf_response = response
        if response == "True":
            st.session_state.tf_feedback = "✅ Correct! This is a linear equation because the variable is raised only to the power of 1."
        else:
            st.session_state.tf_feedback = "❌ Incorrect. This is a linear equation because the highest power of x is 1."
    if st.session_state.tf_response:
        st.info(st.session_state.tf_feedback)

# --- SECTION 2: Objective Checkboxes ---
def objective_selection_step():
    st.subheader("🎯 Step 2: Objectives for Linear Equations")
    st.markdown("**What are the possible objectives/instructions for a linear equation?**")
    st.markdown("☑️ *Uncheck incorrect objectives. Leave all correct ones checked.*")

    correct = [
        "Solve for x", "Graph the equation", "Convert to standard form",
        "Write from two points", "Find intercepts", "Verify solution", "Model real-world scenarios"
    ]
    wrong = st.session_state.distractors_shuffled
    combined = correct + wrong
    random.shuffle(combined)

    selections = {}
    for choice in combined:
        if choice not in st.session_state.checkbox_states:
            st.session_state.checkbox_states[choice] = True  # ✅ All boxes start checked
        selections[choice] = st.checkbox(choice, value=st.session_state.checkbox_states[choice], key=choice)

    if st.button("Check Objectives"):
        incorrect_unchecked = [c for c in correct if not selections[c]]
        incorrect_checked = [d for d in wrong if selections[d]]

        if incorrect_checked:
            st.error("❌ You checked one or more incorrect objectives.")
        elif incorrect_unchecked:
            st.warning("⚠️ You missed one or more correct objectives.")
        else:
            st.success("✅ Excellent! You correctly left all valid objectives checked and removed all invalid ones.")

# --- RUN MODULES ---
type_identification_step()
st.markdown("---")
objective_selection_step()
