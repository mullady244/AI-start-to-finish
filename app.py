
import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Algebra Map", layout="wide")

# Load CSVs
@st.cache_data
def load_data():
    equations = pd.read_csv("equations.csv")
    inequalities = pd.read_csv("inequalities.csv")
    functions = pd.read_csv("functions.csv")
    return equations, inequalities, functions

equations, inequalities, functions = load_data()

# Sidebar
st.sidebar.title("Algebra Navigator")
section = st.sidebar.radio("Choose a Category", ["Equations", "Inequalities", "Functions"])

# Choose dataset based on section
data_map = {
    "Equations": equations,
    "Inequalities": inequalities,
    "Functions": functions
}

df = data_map[section]

# Show types
st.title(f"{section} Explorer")
selected_type = st.selectbox(f"Choose a {section[:-1]} Type", df['Type'].unique())

selected_row = df[df['Type'] == selected_type].iloc[0]

st.subheader("🔹 Objectives")
for obj in selected_row['Objectives'].split(";"):
    st.markdown(f"- {obj.strip()}")

st.subheader("🔸 Solution Types")
for sol in selected_row['Solutions'].split(";"):
    st.markdown(f"- {sol.strip()}")

st.subheader("🛠️ Methods")
for method in selected_row['Methods'].split(";"):
    st.markdown(f"- {method.strip()}")

st.info("✅ More features coming soon: Glossary links, Step-by-step viewers, and Interactive examples.")
