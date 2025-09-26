# COVID-19 Research Metadata Analysis

This repository contains Python scripts and visualizations for analyzing a dataset of COVID-19 research papers. The main focus is on exploring metadata such as publication dates, journals, and paper titles.

## Files

- **app.py**: Streamlit web application for interactive exploration of the dataset. Features include:
  - Data overview and sample display
  - Publications over time (line chart)
  - Top publishing journals (bar chart)
  - Word cloud of paper titles
  - Interactive widgets for filtering by year and number of journals
- **dataAnalysis.py**: Additional data analysis and visualization scripts.
- **metadata.csv**: The dataset containing metadata for COVID-19 research papers.
- **paper_source_distribution.png**: Visualization of paper sources.
- **publications_over_time.png**: Visualization of publication trends over time.
- **title_wordcloud.png**: Word cloud of paper titles.
- **top_journals.png**: Bar chart of top publishing journals.

## How to Run the Streamlit App and Data Analysis App

1. Install required packages:
   ```powershell
   pip install pandas numpy matplotlib seaborn wordcloud streamlit
   ```
2. Launch the apps:
   ```powershell
   streamlit run app.py
   python dataAnalysis.py
   ```
   **Note: Ensure that metadata.csv is in the same directory as the scripts**.

## Features

- Interactive dashboard for exploring COVID-19 research metadata
- Data cleaning and preprocessing
- Visualizations for publication trends, journal distribution, and title word cloud

## Requirements
- Python 3.7+
- pandas, numpy, matplotlib, seaborn, wordcloud, streamlit

## License
This project is for educational purposes.