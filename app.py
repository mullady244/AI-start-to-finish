from datetime import datetime
import streamlit as st
import random

# --- PAGE SETUP ---
st.set_page_config(page_title="Algebra Map – Test XI", layout="wide")
st.title("📘 Algebra Map – Version: Test XI")
st.caption(f"🕒 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.markdown("---")

# --- SESSION STATE SETUP ---
if "objectives_checked" not in st.session_state:
    st.session_state.objectives_checked = []
if "distractors_shuffled" not in st.session_state:
    st.session_state.distractors_shuffled = random.sample([
        "Find cube root", "Calculate standard deviation", "Plot sinusoidal curve",
        "Factor a trinomial", "Graph a logarithmic curve", "Use imaginary numbers"
    ], 3)
if "tf_response" not in st.session_state:
    st.session_state.tf_response = None
if "tf_feedback" not in st.session_state:
    st.session_state.tf_feedback = ""

# --- SECTION 1: TYPE IDENTIFICATION (T/F) ---
def type_identification_step():
    st.subheader("🔍 Step 1: Type Identification")
    st.markdown("Is the following a **Linear Equation**?")
    st.latex("3x + 5 = 14")

    response = st.radio("True or False?", ["True", "False"], key="tf_radio")
    if st.button("Submit T/F Answer"):
        st.session_state.tf_response = response
        if response == "True":
            st.session_state.tf_feedback = "✅ Correct! This is a linear equation because the variable is raised only to the power of 1."
        else:
            st.session_state.tf_feedback = "❌ Incorrect. This is a linear equation because the highest power of x is 1."
    if st.session_state.tf_response:
        st.info(st.session_state.tf_feedback)

# --- SECTION 2: OBJECTIVE SELECTION (MULTI-CHECKBOX) ---
def objective_selection_step():
    st.subheader("🎯 Step 2: Objectives for Linear Equations")
    st.markdown("**What are the possible objectives/instructions for a linear equation?**")
    st.markdown("🔘 *Check all that apply*")

    correct_objectives = [
        "Solve for x", "Graph the equation", "Convert to standard form",
        "Write from two points", "Find intercepts", "Verify solution", "Model real-world scenarios"
    ]
    distractors = st.session_state.distractors_shuffled
    all_choices = correct_objectives + distractors
    random.shuffle(all_choices)

    selected = st.multiselect("Choose all valid objectives:", options=all_choices)

    incorrect_unchecked = [d for d in distractors if d not in selected]
    correct_unchecked = [c for c in correct_objectives if c not in selected]
    incorrect_checked = [d for d in distractors if d in selected]

    if st.button("Check My Selection"):
        if incorrect_checked:
            st.error("❌ You selected one or more incorrect objectives.")
        elif correct_unchecked:
            st.warning("⚠️ You missed one or more correct objectives.")
        else:
            st.success("✅ Great job! You correctly selected all valid objectives and avoided the incorrect ones.")

# --- LOAD MODULES ---
type_identification_step()
st.markdown("---")
objective_selection_step()
