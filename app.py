
import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(page_title="Algebra Map", layout="wide")

# Version info
st.title("📘 Algebra Map – Version: Test 19")

# Section Header
st.header("🔢 Linear Equation Flow")

# Intro message
st.markdown("This is a conceptual exploration, not a solving practice space. Here we explain how to solve, not solve it for you.")
st.markdown("💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.")

# Type Identification Section
st.subheader("🔍 Type Identification")
st.latex("3x + 5 = 14")
st.markdown("The equation above is a Linear Equation.")

# Timestamp
st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
