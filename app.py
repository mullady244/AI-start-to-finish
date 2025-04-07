
import streamlit as st

# Page configuration
st.set_page_config(page_title="AI Start to Finish - Test I", layout="wide")

# Version control setup
CURRENT_VERSION = "Test I"

# Title with versioning
st.title("📘 Algebra Map – Version: " + CURRENT_VERSION)

# Notification for update (Option B)
st.warning("🔄 A new version is available. Click below to refresh.")
if st.button("Refresh Now"):
    st.experimental_rerun()

# Sample content for linear equations (placeholder)
st.header("🔢 Linear Equation Flow")
st.latex("3x + 5 = 14")
st.markdown("This is a conceptual exploration, not a solving practice space. Here we explain how to solve, not solve it for you.")

# Educational philosophy reminder
st.info("💡 This app guides you through the conceptual structure of Algebra. Solving is for your notebook. Mastery is for your mind.")

# Footer
st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
