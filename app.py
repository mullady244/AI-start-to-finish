
import streamlit as st

st.set_page_config(page_title="Linear Equation Learning Flow", layout="wide")

# Title
st.title("🔢 Linear Equation Learning Flow")

# Section 1: Identify the Expression Type
st.header("1️⃣ Identify the Expression Type")
st.markdown("**What kind of mathematical statement is this?**")

question_1 = st.radio("`3x + 5 = 14` is a...", ["Expression", "Equation", "Inequality", "Function"])
if question_1:
    if question_1 == "Equation":
        st.success("✅ Correct! It's an equation because it has an equals sign.")
    else:
        st.error("❌ Not quite. This is an **equation** because it contains an equals sign.")

# Section 2: Choose Your Objective
st.header("2️⃣ Choose Your Objective with This Linear Equation")
objective = st.selectbox("Select what you'd like to do with it:", [
    "Solve for x",
    "Graph it",
    "Find the y-intercept",
    "Model a real-world situation"
])
st.info(f"🔍 Selected Objective: {objective}")

# Section 3: Solutions
st.header("3️⃣ What Kind of Solution Can Linear Equations Have?")
st.markdown("Linear equations have one of the following solution types:")

st.markdown("- ✅ One real solution")
st.markdown("- 🚫 No solution (if both sides are parallel but different)")
st.markdown("- ♾️ Infinite solutions (if both sides are exactly the same)")

solution_quiz = st.radio("What is the solution to `2x + 3 = 2x + 5`?", ["One solution", "No solution", "Infinite solutions"])
if solution_quiz:
    if solution_quiz == "No solution":
        st.success("✅ Correct. The variable terms cancel, and you're left with `3 = 5` which is false.")
    else:
        st.error("❌ Incorrect. If the variable cancels and you're left with a false statement, there is **no solution**.")

# Section 4: Methods
st.header("4️⃣ Solving Methods for Linear Equations")
with st.expander("🔧 View Solving Methods"):
    st.markdown("- **Inverse Operations** (add/subtract, multiply/divide)")
    st.markdown("- **Graphing**")
    st.markdown("- **Technology tools** (calculators, algebra software)")
    st.markdown("- **Verbal ↔ Symbolic modeling**")

# Section 5: Step-by-Step Problem
st.header("5️⃣ Solve This: `3x - 5 = 10`")
user_answer = st.text_input("What is the value of x?")

if user_answer:
    try:
        if float(user_answer) == 5:
            st.success("🎉 Correct! `3x = 15` → `x = 5`")
        else:
            st.error("❌ Try again. Remember to add 5 to both sides, then divide by 3.")
    except:
        st.warning("⚠️ Please enter a number.")

# Section 6: Common Mistake
st.header("6️⃣ Common Mistake Insight")
st.markdown("In the equation `2x + 3 = 2x + 5`, many mistakenly subtract `2x` and say the answer is `3 = 5`, which leads them to assume a solution exists. But `3 = 5` is false, so this equation has **no solution**.")

# Section 7: Glossary (Conceptual Terms)
st.header("📘 Key Terms to Know")
with st.expander("🧠 View Glossary"):
    st.markdown("- **Equation**: A mathematical sentence that asserts two expressions are equal.")
    st.markdown("- **Linear Equation**: An equation where the variable is to the first power and graphs as a straight line.")
    st.markdown("- **Inverse Operation**: The opposite operation used to isolate the variable.")
    st.markdown("- **Solution**: A value for the variable that makes the equation true.")

# Section 8: Essay Reflection
st.header("📝 Explain It Back")
st.text_area("In your own words, explain how to solve a linear equation and what types of solutions are possible.")

# Footer
st.markdown("---")
st.caption("🔧 Powered by AI | Designed for Conceptual Understanding | 'AI-Start-to-Finish'")
