import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Job dashboard", page_icon=":barchart:",layout="wide")

st.title(" :bar_chart: Job Dashboard")
st.markdown('<style>div.block-container{padding-top: 1rem}</style>',unsafe_allow_html=True)

os.chdir(r"D:\dung\HUST\20231\BigData\visualize")
df = pd.read_json("job-analysis.careerbuilder.json")

st.title("Job Distribution Across Industries")


industry = st.multiselect("pick your industry",df["industry"].unique())
if not industry:
    industry_counts = df.copy()
else:
    industry_counts = df[df["industry"].isin(industry)]
    
industry_counts = industry_counts["industry"].value_counts().reset_index()
industry_counts.columns = ['industry', 'count']

col1, col2 = st.columns((2))


with col1:
    st.subheader(f"Number of Jobs in Each Industry ")
    fig = px.bar(
            industry_counts,
            x='industry',
            y='count',
            text='count', 
            labels={'industry': 'Industry', 'count': 'Number of Jobs'},
            color='industry',
            height=500,
        )
    st.plotly_chart(fig,use_container_width=True, height =300)
    
with col2:
    st.subheader("Percentage of Jobs in Each Industry")
    fig = px.pie(
        industry_counts,
        values='count',
        names='industry',
        labels={'industry': 'Industry'},
        height=500,
    )
    st.plotly_chart(fig,use_container_width=True, height =300)