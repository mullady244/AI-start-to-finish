
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test VI", layout="centered")

# Header
st.title("📘 Algebra Map – Version: Test VI")

# Auto-refresh notice (for visual confirmation)
st.success("✅ You’re viewing the latest version – Test VI")

st.write("🔢 **Linear Equation Learning Flow**")
st.markdown("*This is a conceptual exploration space. We teach how to solve, but you solve in your notebook.*")
st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# -----------------------
# Step 1: Rotating T/F questions (from pool)
# -----------------------

st.subheader("🔍 Step 1: Identify the Mathematical Statement Type")

tf_questions = [
    ("3x + 5 = 14 is a linear equation.", True),
    ("y = 2x² + 1 is a linear equation.", False),
    ("x² = 9 is a linear equation.", False),
    ("y = mx + b is the general form of a linear equation.", True),
    ("A linear equation always has two variables.", False)
]

selected_question = random.choice(tf_questions)
question_text, correct_answer = selected_question

st.write("**Statement:** " + question_text)
user_tf = st.radio("True or False?", ["True", "False"], key="tf_q")

if st.button("Check Answer"):
    if (user_tf == "True" and correct_answer) or (user_tf == "False" and not correct_answer):
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect.")
        st.markdown("**Explanation:** " + (
            "This is correct because it matches the definition of a linear equation."
            if correct_answer else
            "This is incorrect because it's not in the form of a linear equation (e.g., includes squares or curves)."
        ))

# -----------------------
# Step 2A: Immediate Objective
# -----------------------

st.subheader("🎯 Step 2A: What is the Given Objective?")

st.markdown("""
*Imagine you're given this equation:*  
**3x + 5 = 14**
""")

st.radio("What is the objective?", [
    "Simplify the expression",
    "Solve for x",
    "Evaluate at x = 5",
    "Graph this equation"
], key="objective_q")

st.info("💡 On tests and in life, the objective is not chosen — it's given. Algebra helps you respond correctly.")

# -----------------------
# Step 2B: Broader Objectives
# -----------------------

st.subheader("🧭 Step 2B: What are *other* possible objectives for linear equations?")

st.multiselect("Select all that apply:", [
    "Solve for x",
    "Graph the equation",
    "Convert to standard form",
    "Write from two points",
    "Find intercepts",
    "Verify solution",
    "Model real-world scenarios"
], key="multi_objective_q")

st.caption("Not all objectives apply at once. But knowing what's *possible* strengthens your readiness.")
