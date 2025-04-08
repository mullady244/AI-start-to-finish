
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test VII", layout="centered")

# Header
st.title("📘 Algebra Map – Version: Test VII")

st.success("✅ You’re viewing the latest version – Test VII")
st.write("🔢 **Linear Equation Learning Flow**")
st.markdown("*This is a conceptual exploration space. We teach how to solve, but you solve in your notebook.*")
st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# -----------------------
# Step 1: Identify Type (T/F)
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
# Step 2: Explore All Objectives
# -----------------------

st.subheader("🎯 Step 2: What are the Objectives or Instructions for Linear Equations?")

# All real linear objectives
valid_objectives = [
    "Solve for x",
    "Graph the equation",
    "Convert to standard form",
    "Write from two points",
    "Find intercepts",
    "Verify solution",
    "Model real-world scenarios"
]

# Irrelevant distractor options (3 rotate each time)
distractor_pool = [
    "Factor the trinomial",
    "Find the vertex",
    "Simplify a radical expression",
    "Solve the quadratic",
    "Determine end behavior",
    "Calculate standard deviation",
    "Find the period and amplitude",
    "Identify the asymptotes",
    "Use the quadratic formula",
    "Rewrite in vertex form"
]

distractors = random.sample(distractor_pool, 3)

# Combine and shuffle
all_choices = valid_objectives + distractors
random.shuffle(all_choices)

st.write("Click all that apply:")
selected = st.multiselect("Linear Equations – Possible Objectives", all_choices, key="obj_q")

st.caption("💡 Knowing what's possible keeps you ready for *any* instruction on a test or in real life.")
