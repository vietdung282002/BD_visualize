import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_json("job-analysis.careerbuilder.json")
filtered_df = df[df['job_requirement']!=""]
all_skills = ' '.join(filtered_df['job_requirement'])

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_skills)

# Plot the Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for skill Column')

st.pyplot(plt)