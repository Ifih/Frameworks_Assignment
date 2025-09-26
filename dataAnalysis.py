import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from wordcloud import WordCloud
import streamlit as st

# --<< Data Loading and Basic Exploration >>--
print("--<< Data Loading and Basic Exploration >>--")

# Load the data
try:
    df = pd.read_csv('metadata.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: 'metadata.csv' not found. Please make sure the file is in the same directory.")
    exit()

# Examine the first few rows and data structure
print("\nFirst 5 rows of the DataFrame:")
print(df.head())

# Basic data exploration
print("\nDataFrame dimensions (rows, columns):", df.shape)
print("\nData types of each column:")
print(df.info())

# Check for missing values
print("\nMissing values in key columns:")
print(df[['title', 'abstract', 'publish_time', 'journal']].isnull().sum())

print("\nMissing values per column:")
print(df.isnull().sum())

# Generate basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(df.describe())

# --<< Data Cleaning and Preparation >>--
print("\n---<< Data Cleaning and Preparation >>--")

# Handle missing data
# Identify columns with many missing values
missing_values_count = df.isnull().sum()
print("\nColumns with missing values:\n", missing_values_count[missing_values_count > 0])

# Create a cleaned version of the dataset
df_cleaned = df.dropna(subset=['title', 'abstract', 'publish_time', 'journal']).copy()
print(f"\nOriginal shape: {df.shape}, Cleaned shape: {df_cleaned.shape}")

# Prepare data for analysis
# Convert date columns to datetime format
df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')
df_cleaned.dropna(subset=['publish_time'], inplace=True)

# Extract year from publication date
df_cleaned['publish_year'] = df_cleaned['publish_time'].dt.year

# Create new columns if needed (e.g., abstract word count)
df_cleaned['abstract_word_count'] = df_cleaned['abstract'].apply(lambda x: len(str(x).split()))
print("\nNew columns added: 'publish_year', 'abstract_word_count'")
print(df_cleaned.head())

# --<< Data Analysis and Visualization >>--
print("\n--<< Data Analysis and Visualization >>--")

# Perform basic analysis
# Count papers by publication year
papers_by_year = df_cleaned['publish_year'].value_counts().sort_index()
print("\nNumber of papers by publication year:\n", papers_by_year)

# Identify top journals publishing COVID-19 research
top_journals = df_cleaned['journal'].value_counts().head(10)
print("\nTop 10 publishing journals:\n", top_journals)

# Find most frequent words in titles (using simple word frequency)
all_titles = ' '.join(df_cleaned['title'].str.lower())
words = re.findall(r'\b\w+\b', all_titles)
# Remove common English stop words and single-letter words
stop_words = set(['the', 'and', 'of', 'in', 'a', 'to', 'for', 'with', 'on', 'is', 'as', 'by', 'from', 'an', 'at'])
filtered_words = [word for word in words if word not in stop_words and len(word) > 1]
word_counts = Counter(filtered_words)
print("\nTop 20 most frequent words in titles:")
print(word_counts.most_common(20))

# Create visualizations
# Plot number of publications over time
plt.figure(figsize=(12, 6))
papers_by_year.plot(kind='line', marker='o')
plt.title('Number of COVID-19 Publications Over Time')
plt.xlabel('Publication Year')
plt.ylabel('Number of Papers')
plt.grid(True)
plt.tight_layout()
plt.savefig('publications_over_time.png')
print("\nPlot saved as 'publications_over_time.png'")

# Create a bar chart of top publishing journals
plt.figure(figsize=(12, 8))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis')
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Number of Papers')
plt.ylabel('Journal')
plt.tight_layout()
plt.savefig('top_journals.png')
print("Bar chart saved as 'top_journals.png'")

# Generate a word cloud of paper titles
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of COVID-19 Paper Titles')
plt.tight_layout()
plt.savefig('title_wordcloud.png')
print("Word cloud saved as 'title_wordcloud.png'")

# Plot distribution of paper counts by source
plt.figure(figsize=(10, 6))
df_cleaned['source_x'].value_counts().plot(kind='bar')
plt.title('Distribution of Paper Counts by Source')
plt.xlabel('Source')
plt.ylabel('Number of Papers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('paper_source_distribution.png')
print("Bar chart of paper source distribution saved as 'paper_source_distribution.png'")