
import streamlit as st
import datetime

# Page configuration
st.set_page_config(page_title="AI Start to Finish - Test IV", layout="wide")

# Version control
CURRENT_VERSION = "Test IV"

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

st.markdown("### 🔍 Step 1: Identify the Type of Mathematical Statement")
st.latex("3x + 5 = 14")
st.markdown("Is this a linear equation, inequality, or function?")

# Multiple choice for identification
user_answer = st.radio(
    "What type of mathematical statement is this?",
    ["Linear Equation", "Linear Inequality", "Linear Function", "None of the above"]
)

# Feedback
if user_answer:
    if user_answer == "Linear Equation":
        st.success("✅ Correct! This is a linear equation. It includes an equals sign and the variable has degree 1.")
    else:
        st.error("❌ Not quite. This is a **linear equation** because it has an equals sign and its highest exponent is 1.")

# Footer
st.info("💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.")
st.caption("Last updated: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
