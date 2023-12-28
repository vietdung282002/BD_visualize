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
numeric_columns = ["salary_min", "salary_max", "job_yoe_min", "job_yoe_max"]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")
df["salary_min"] = pd.to_numeric(df["salary_min"], errors="coerce")/1000000
df["salary_max"] = pd.to_numeric(df["salary_max"], errors="coerce")/1000000
df = df[(df["salary_min"] < 100) & (df["salary_max"] < 100)]

col1, col2 = st.columns((2))
# Scatter plot with color normalization
with col1:
    fig, ax = plt.subplots()
    sc = ax.scatter(df["salary_min"], df["salary_max"], c=df["job_yoe_min"], cmap="viridis", s=100, alpha=0.75, marker='o')
    ax.set_xlabel("Min Salary (triệu VND)")
    ax.set_ylabel("Max Salary (triệu VND)")
    ax.set_title("Scatter Plot of Salary Ranges with Years of Experience")

    # Add colorbar
    cbar = plt.colorbar(sc, ax=ax, label="Years of Experience (Min)")

    # Display the scatter plot using Streamlit
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    sc = ax.scatter(df["salary_min"], df["salary_max"], c=df["job_yoe_max"], cmap="viridis", s=100, alpha=0.75, marker='o')
    ax.set_xlabel("Min Salary (triệu VND)")
    ax.set_ylabel("Max Salary (triệu VND)")
    ax.set_title("Scatter Plot of Salary Ranges with Years of Experience")

    # Add colorbar
    cbar = plt.colorbar(sc, ax=ax, label="Years of Experience (Max)")

    # Display the scatter plot using Streamlit
    st.pyplot(fig)
