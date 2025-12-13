import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chemical Safety Database", layout="wide")

st.title("🧪 Chemical Safety Database")

# Load data
df = pd.read_excel("chemicals.xlsx")

# Search bar
search = st.text_input("Search chemical name:")

if search:
    result = df[df["ChemicalName"].str.contains(search, case=False, na=False)]
else:
    result = df

# Display table
st.dataframe(result)
