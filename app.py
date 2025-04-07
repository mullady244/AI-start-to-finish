import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Start to Finish", layout="wide")
st.title("🔢 Linear Equation Learning Flow")

# Section 1: Identify the Type
st.header("1️⃣ Identify the Type")
st.markdown("**Question:** What kind of mathematical statement is this?\n\n`y = 2x + 3`")
type_answer = st.radio("Choose one:", ["Linear Equation", "Quadratic Equation", "Rational Expression", "Inequality"])
if type_answer:
    if type_answer == "Linear Equation":
        st.success("✅ Correct! This is a linear equation in slope-intercept form.")
    else:
        st.error("❌ Incorrect. This is a linear equation — the variable x is raised only to the first power.")

# Section 2: Objectives
st.header("2️⃣ Select an Objective")
objective = st.selectbox("What are we trying to do with this linear equation?", [
    "Solve for x",
    "Graph the equation",
    "Find the slope",
    "Model a real-world scenario"
])

# Section 3: Solutions
st.header("3️⃣ Understand Possible Solutions")
st.markdown("Linear equations can have:")
st.markdown("- ✅ One real solution\n- 🚫 No solution\n- 🔁 Infinite solutions")
st.markdown("**Example:** What does `2x + 3 = 2x + 5` imply?")
solution_example = st.radio("Choose the best answer:", [
    "One real solution", "No solution", "Infinite solutions"
])
if solution_example:
    if solution_example == "No solution":
        st.success("✅ Correct! The variables cancel, and you're left with a false statement (3 ≠ 5).")
    else:
        st.error("❌ Not quite. When the variable terms cancel but constants are unequal, there’s no solution.")

# Section 4: Method
st.header("4️⃣ Choose a Method")
st.markdown("To solve linear equations, we typically use:")
st.markdown("- Inverse operations\n- Graphing\n- Technology\n- Verbal ↔ Symbolic Modeling")
method_check = st.checkbox("Click to reveal step-by-step for Inverse Operations")
if method_check:
    st.subheader("🪜 Step-by-Step: Inverse Operations")
    st.markdown("""
    **Step 1:** Simplify both sides (expand, combine like terms)  
    **Step 2:** Use addition/subtraction to isolate the variable term  
    **Step 3:** Use multiplication/division to isolate the variable  
    **Step 4:** Check your solution in the original equation
    """)
    st.markdown("**Mini Quiz:** Solve `3x - 5 = 10`. What is x?")
    x_value = st.text_input("x = ?")
    if x_value:
        if x_value.strip() == "5":
            st.success("✅ Correct! Adding 5 to both sides, then dividing by 3 gives x = 5.")
        else:
            st.error("❌ Not quite. Try isolating x step by step.")

# Section 5: Common Mistake
st.header("5️⃣ Common Mistake Insight")
st.markdown("**Mistake:** Solving `2x + 3 = 2x + 5` and saying x = 1.")
st.markdown("**Why it’s wrong:** The x terms cancel out — you're left with 3 = 5, which is false. So there’s no solution.")

# Section 6: Concept Glossary
st.header("6️⃣ Glossary Terms in Context")
with st.expander("📘 Tap to reveal key terms"):
    st.markdown("""
    - **Linear Equation**: An equation where the highest power of the variable is 1.
    - **Inverse Operations**: Operations that undo each other (e.g., add/subtract, multiply/divide).
    - **Slope-Intercept Form**: Form y = mx + b where m is slope, b is y-intercept.
    - **No Solution**: A contradiction like 3 = 5 that makes the equation false.
    """)

# Section 7: Optional Graph
st.header("7️⃣ Optional Visual")
st.markdown("Imagine the graph of `y = 2x + 3` — a straight line with slope 2 and y-intercept 3.")

# Section 8: Wrap-Up Essay (Optional)
st.header("8️⃣ Essay Challenge")
st.markdown("**Write your own explanation:** Why does `3x - 5 = 10` have one solution, and how would you find it?")
user_essay = st.text_area("Your explanation:")
if user_essay:
    st.success("💬 Thanks for explaining! This helps reinforce your mastery.")
