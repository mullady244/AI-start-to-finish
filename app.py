
import streamlit as st

# App Configuration
st.set_page_config(page_title="Algebra Map – Version: Test 20", layout="centered")

# Header
st.title("📘 Algebra Map – Version: Test 20")
st.header("🔢 Linear Equation Flow")

st.markdown("This is a conceptual exploration, not a solving practice space. Here we explain how to solve, not solve it for you.")
st.markdown("💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.")

# Type Identification Section
st.subheader("🔍 Type Identification")
st.latex("3x + 5 = 14")
st.write("The equation above is a Linear Equation.")

# T/F Question
st.markdown("**True or False?**")
true_false_response = st.radio(
    "Select your answer:",
    options=["", "True", "False"],
    index=0,
    key="tf_question"
)

# Feedback after selection
if true_false_response == "True":
    st.success("✅ Correct! This is a linear equation.")
elif true_false_response == "False":
    st.error("❌ Incorrect. This is a linear equation.")

# Footer
st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
