
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Algebra Map – Version: Test 21", layout="wide")

st.title("📘 Algebra Map – Version: Test 21")

st.header("🔢 Linear Equation Flow")
st.markdown("This is a conceptual exploration, not a solving practice space. Here we explain how to solve, not solve it for you.")
st.markdown("💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.")

st.subheader("🔍 Type Identification")

# Display the equation only once
st.latex("3x + 5 = 14")

# True or False question with placeholder
tf_options = ["Select an answer...", "True", "False"]
tf_response = st.radio("The equation above is a Linear Equation.", tf_options, index=0)

# Response validation
if tf_response != "Select an answer...":
    if tf_response == "True":
        st.success("✅ Correct! This is a linear equation because the variable has an exponent of 1.")
    else:
        st.error("❌ Incorrect. This is actually a linear equation because the variable has an exponent of 1.")

# Footer timestamp
st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
