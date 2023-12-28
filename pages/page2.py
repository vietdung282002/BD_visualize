import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')

df = pd.read_json("job-analysis.careerbuilder.json")




# Filter the DataFrame based on the selected employment type
industry = st.multiselect("pick your industry",df["industry"].unique())
if not industry:
    filtered_df = df.copy()
else:
    filtered_df = df[df["industry"].isin(industry)]

# Count the occurrences of each employment type
job_level_counts = filtered_df["job_level"].value_counts().reset_index()

st.dataframe(job_level_counts)
# Plotting the bar chart
col1, col2 = st.columns((2))


with col1:
    fig = px.bar(
            job_level_counts,
            x='job_level',
            y='count',
            text='count', 
            labels={'job_level': 'job_level', 'count': 'Number of Jobs'},
            color='job_level',
            height=500,
        )
    st.plotly_chart(fig,use_container_width=True, height =300)
    
with col2:
    fig = px.pie(
        job_level_counts,
        values='count',
        names='job_level',
        labels={'job_level': 'job_level'},
        height=500,
    )
    st.plotly_chart(fig,use_container_width=True, height =300)