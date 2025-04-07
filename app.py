
import streamlit as st
import datetime

# Page configuration
st.set_page_config(page_title="AI Start to Finish - Test V", layout="wide")

# Version control
CURRENT_VERSION = "Test V"

# Title
st.title("📘 Algebra Map – Version: " + CURRENT_VERSION)

# Smart refresh logic
if "just_refreshed" not in st.session_state:
    st.session_state["just_refreshed"] = False

if st.session_state["just_refreshed"]:
    st.success("✅ You are now running the latest version!")
    st.session_state["just_refreshed"] = False
else:
    st.warning("🔄 A new version is available. Click below to refresh.")
    if st.button("Refresh Now"):
        st.session_state["just_refreshed"] = True
        st.rerun()

# Section: Conceptual Flow for Linear Equations
st.header("🔢 Linear Equation Flow")

# Step 1: Identify the Type
st.subheader("🔍 Step 1: Identify the Type of Mathematical Statement")
st.latex("3x + 5 = 14")
st.markdown("Is this a linear equation, inequality, or function?")

answer_type = st.radio(
    "What type of mathematical statement is this?",
    ["Linear Equation", "Linear Inequality", "Linear Function", "None of the above"],
    key="step1"
)

if answer_type:
    if answer_type == "Linear Equation":
        st.success("✅ Correct! This is a linear equation. It has an equals sign and the variable is to the first power.")
    else:
        st.error("❌ Not quite. This is a **linear equation** due to the equals sign and linear degree of the variable.")

# Step 2: Choose Objective
st.subheader("🎯 Step 2: What Is the Objective?")
st.markdown("What are you being asked to do with this equation?")

answer_objective = st.radio(
    "Choose the objective:",
    [
        "Solve for x",
        "Graph the inequality",
        "Simplify the expression",
        "Evaluate the function at x = 3"
    ],
    key="step2"
)

if answer_objective:
    if answer_objective == "Solve for x":
        st.success("✅ Exactly. When you're presented with an equation like this, you're being asked to solve for the unknown.")
    else:
        st.error("❌ Not quite. This is a **linear equation**, so the goal is to **solve for x** — not to evaluate, simplify, or graph.")

# Footer
st.info("💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.")
st.caption("Last updated: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
