
import streamlit as st

st.set_page_config(page_title="Linear Equation Learning Flow", layout="wide")

# Title
st.title("🔢 Linear Equation Learning Flow")

# Section 1: Identify the Expression Type
st.header("1️⃣ Identify the Expression Type")
st.markdown("**What kind of mathematical statement is this?**")

st.latex("3x + 5 = 14")

question_1 = st.radio("This is a...", ["Expression", "Equation", "Inequality", "Function"])
if question_1:
    if question_1 == "Equation":
        st.success("✅ Correct! It's an equation because it has an equals sign.")
    else:
        st.error("❌ Not quite. This is an **equation** because it contains an equals sign.")

# Section 2: Choose Your Objective
st.header("2️⃣ Choose Your Objective with This Linear Equation")
objective = st.selectbox("Select what you'd like to do with it:", [
    "Understand how to solve for x (conceptually)",
    "Understand how to graph it (conceptually)",
    "Understand the y-intercept",
    "Understand how it models a real-world situation"
])
st.info(f"🔍 Selected Objective: {objective}")

# Section 3: Solutions
st.header("3️⃣ What Kind of Solution Can Linear Equations Have?")
st.markdown("Linear equations can result in the following:")

st.markdown("- ✅ One real solution")
st.markdown("- 🚫 No solution (parallel lines with different intercepts)")
st.markdown("- ♾️ Infinite solutions (identical expressions on both sides)")

st.latex("2x + 3 = 2x + 5")
solution_quiz = st.radio("This equation has...", ["One solution", "No solution", "Infinite solutions"])
if solution_quiz:
    if solution_quiz == "No solution":
        st.success("✅ Correct. Simplifies to a false statement `3 = 5`, so no solution.")
    else:
        st.error("❌ Incorrect. Try simplifying both sides. If the variable cancels and the result is false, there's **no solution**.")

# Section 4: Methods (Conceptual)
st.header("4️⃣ Conceptual Methods for Solving Linear Equations")
with st.expander("🔧 View Conceptual Methods"):
    st.markdown("- **Inverse Operations** (reverse the operations to isolate variable)")
    st.markdown("- **Graphing** (intersecting line shows the solution visually)")
    st.markdown("- **Technology Tools** (desmos, calculator, etc.)")
    st.markdown("- **Verbal ↔ Symbolic Modeling** (translate real-world problems into equations)")

# Section 5: Conceptual Walkthrough
st.header("5️⃣ Conceptual Walkthrough Example")

st.latex("3x - 5 = 10")
st.markdown("**Step 1:** Add 5 to both sides to cancel the -5.")
st.markdown("**Step 2:** Divide both sides by 3 to isolate x.")
st.markdown("No need to solve it — just understand the inverse operations used to isolate the variable.")

# Section 6: Common Mistake
st.header("6️⃣ Common Mistake Insight")
st.markdown("In the equation:")
st.latex("2x + 3 = 2x + 5")
st.markdown("Many mistakenly cancel `2x` and think a solution exists.")
st.markdown("However, you get `3 = 5` — which is false. So, this equation has **no solution**.")

# Section 7: Glossary (Key Conceptual Terms)
st.header("📘 Key Terms to Know")
with st.expander("🧠 View Glossary"):
    st.markdown("- **Equation**: A mathematical sentence asserting equality between two expressions.")
    st.markdown("- **Linear Equation**: Variable is raised to the first power and graphs a straight line.")
    st.markdown("- **Inverse Operation**: The opposite operation used to isolate a variable.")
    st.markdown("- **Solution**: A value that makes the equation true.")

# Section 8: Explain It Back (locked for now)
st.header("📝 Explain It Back (Final Phase)")
st.markdown("🔒 Locked until you've completed True/False and Multiple Choice sections with 100% accuracy.")
st.markdown("_This section is part of a multi-phase testing system designed to promote true conceptual mastery._")

# Footer
st.markdown("---")
st.caption("🔧 Powered by AI | Designed for Conceptual Understanding | 'AI-Start-to-Finish'")
