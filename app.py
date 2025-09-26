import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from wordcloud import WordCloud
import streamlit as st

# --<< Streamlit Application >>--
print("\n--<< Streamlit Application >>--")

# Streamlit app code
st.title('COVID-19 Research Metadata Analysis')
st.write('An interactive dashboard for exploring a dataset of COVID-19 research papers.')

# Load data for the app
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv')
    df_cleaned = df.dropna(subset=['title', 'abstract', 'publish_time', 'journal']).copy()
    df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')
    df_cleaned.dropna(subset=['publish_time'], inplace=True)
    df_cleaned['publish_year'] = df_cleaned['publish_time'].dt.year
    return df_cleaned

df_app = load_data()

st.header('Data Overview')
st.write(f"Total papers in cleaned dataset: {len(df_app)}")
st.write("Sample of the data:")
st.dataframe(df_app.head())

# Interactive widget: Slider for year range
st.header('Publications Over Time')
min_year, max_year = int(df_app['publish_year'].min()), int(df_app['publish_year'].max())
year_range = st.slider(
    'Select a year range:',
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)
filtered_df = df_app[(df_app['publish_year'] >= year_range[0]) & (df_app['publish_year'] <= year_range[1])]
papers_by_year_filtered = filtered_df['publish_year'].value_counts().sort_index()
st.line_chart(papers_by_year_filtered)

# Interactive widget: Dropdown for top journals
st.header('Top Publishing Journals')
num_journals = st.slider('Number of top journals to display:', 5, 20, 10)
top_journals_filtered = filtered_df['journal'].value_counts().head(num_journals)
st.bar_chart(top_journals_filtered)

# Display word cloud
st.header('Word Cloud of Paper Titles')
all_titles_filtered = ' '.join(filtered_df['title'].str.lower())
if all_titles_filtered:
    wordcloud_app = WordCloud(width=800, height=400, background_color='white').generate(all_titles_filtered)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud_app, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
else:
    st.write("No titles to display for the selected year range.")

print("\nStreamlit app code generated and included in the script.")
print("Script execution complete.")