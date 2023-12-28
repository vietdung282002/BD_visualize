import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
import seaborn as sns
import ast

warnings.filterwarnings('ignore')

df = pd.read_json("job-analysis.careerbuilder.json")

# Convert salary columns to numeric values, handling "None" values
df["salary_min"] = pd.to_numeric(df["salary_min"], errors="coerce")/1000000
df["salary_max"] = pd.to_numeric(df["salary_max"], errors="coerce")/1000000

# Create a boxplot
filtered_df = df[(df["salary_min"] < 100) & (df["salary_max"] < 100)]


# Create a boxplot
fig, ax = plt.subplots()
ax.boxplot([filtered_df["salary_min"].dropna(), filtered_df["salary_max"].dropna()], labels=["Min Salary", "Max Salary"])
ax.set_title("Salary Distribution")
ax.set_ylabel("Salary (triệu VND)")

# Display the boxplot using Streamlit
st.pyplot(fig)