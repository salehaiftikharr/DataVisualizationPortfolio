# Programming Languages Popularity Tracker

![Dashboard Screenshot](../images/proj1.png)

## What is this project?

This is an interactive dashboard that explores trends across a range of programming languages. It brings together data on how developers feel about different languages (admired vs. desired), how those languages compare in terms of salary, how their popularity has shifted over time, and where they’re most used across industries.

## Why did I build this?

I’ve always been curious about how the tools we use as developers reflect larger trends in the tech world. What languages are loved but not used? Which ones pay well? Are some growing while others fade out? I wanted to build something that answers these questions in a way that’s not overwhelming — something you could actually explore and learn from, even if you're not a data scientist.

## How did I build it?

The dashboard was built using:
- **Python** for all data processing and transformation
- **Pandas** for wrangling and merging multiple datasets
- **Plotly** for interactive charts and visualizations
- **Streamlit** to create the web-based dashboard interface

I pulled data from multiple sources, including developer surveys and public wage datasets, and merged them to show patterns that are often scattered across the internet. Each section of the dashboard focuses on a specific angle — admiration vs. desire, salary insights, decade-long shifts in popularity, and usage by industry.

---

### Tools Used

- Python
- Pandas
- Plotly
- Streamlit
- Canva (for the project thumbnail)

---

### Data Sources

- Stack Overflow Developer Survey 2024
- top_paid_programming_languages_2024.csv
- programming_languages_desired_admired_2024.csv
- language_popularity_2014_vs_2024.csv
- industry_language_usage.csv

---

### Features

- *Interactive dropdown* to explore admiration, desire, and salary for a specific language
- *Historical comparison chart* showing how language popularity changed from 2014 to 2024
- *Industry usage panel* showing where each language is most commonly used
- *Clean reflections section* to summarize key insights and learnings

---

### Want to try it?

Clone the repo, install the requirements, and run:
```bash
streamlit run app.py


---

Let me know if you’d like a version that includes links to actual datasets or a GitHub-friendly version with relative paths!

