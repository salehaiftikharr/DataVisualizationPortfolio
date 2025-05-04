import streamlit as st
import pandas as pd
import plotly.express as px

# Set up the page
st.set_page_config(page_title="Programming Languages Popularity Tracker", layout="wide")
st.title("Programming Languages Popularity Tracker")

# Intro section
st.markdown("""
Welcome to the **Programming Languages Popularity Tracker** — a dashboard created to explore how programming languages are perceived, paid, and used across industries.

---

Drawing from 2024 developer survey data and job market insights, this tool helps visualize:
- How developers *admire* and *desire* different languages
- Salary trends and the admiration gap
- Shifts in programming language popularity over the past decade
- Language usage across sectors like web, finance, mobile, and data science

This project was inspired by trends I explored in my Data Science course, where we discussed how technical preferences intersect with real-world outcomes. Whether you're a developer planning your next step or just curious about tech trends, this dashboard gives a snapshot of the evolving programming landscape.
""")

# ================================
# Admired, Desired & Salary by Language
# ================================
st.markdown("---")
st.header(" Admired, Desired & Salary by Language (2024)")

desired_admired_df = pd.read_csv("programming_languages_desired_admired_2024.csv")
salary_df = pd.read_csv("top_paid_programming_languages_2024.csv")
merged_df = pd.merge(desired_admired_df, salary_df, on="Language")
merged_df["Admiration Gap"] = merged_df["Admired (%)"] - merged_df["Desired (%)"]

selected_language = st.selectbox("Select a language to view admiration, desire, and salary details:", merged_df["Language"].sort_values())
lang_data = merged_df[merged_df["Language"] == selected_language].iloc[0]

st.markdown(f"""
### {selected_language}

- **Admired**: {lang_data['Admired (%)']}%
- **Desired**: {lang_data['Desired (%)']}%
- **Admiration Gap**: {round(lang_data['Admiration Gap'], 1)} percentage points
- **Average Salary**: ${lang_data['Average Salary (USD)']:,}

> A high admiration gap often suggests that a language is respected but less desired—possibly due to complexity, lack of job demand, or steep learning curve.
""")

overall_avg_salary = int(merged_df["Average Salary (USD)"].mean())
highest_salary = merged_df["Average Salary (USD)"].max()
lowest_salary = merged_df["Average Salary (USD)"].min()
highest_lang = merged_df.loc[merged_df["Average Salary (USD)"] == highest_salary, "Language"].values[0]
lowest_lang = merged_df.loc[merged_df["Average Salary (USD)"] == lowest_salary, "Language"].values[0]

st.markdown(f"""
### Salary Context for **{selected_language}**

- **Average Salary for {selected_language}**: ${lang_data['Average Salary (USD)']:,}
- **Overall Average Across Languages**: ${overall_avg_salary:,}
- **Highest Average Salary**: {highest_lang} — ${int(highest_salary):,}
- **Lowest Average Salary**: {lowest_lang} — ${int(lowest_salary):,}

> Compared to other languages, **{selected_language}** earns {"above" if lang_data['Average Salary (USD)'] > overall_avg_salary else "below"} the average.
""")

# ================================
# Programming Language Popularity Shift
# ================================
st.markdown("---")
st.header("Programming Language Popularity Shift (2014–2024)")

compare_df = pd.read_csv("language_popularity_2014_vs_2024.csv")
melted = compare_df.melt(id_vars="Language", value_vars=["2014 (%)", "2024 (%)"],
                         var_name="Year", value_name="Popularity")

fig_compare = px.bar(
    melted,
    x="Language",
    y="Popularity",
    color="Year",
    barmode="group",
    title="Change in Programming Language Popularity (2014 vs 2024)",
    color_discrete_map={"2014 (%)": "#888", "2024 (%)": "#1f77b4"}
)

fig_compare.update_layout(yaxis_title="Popularity (% of SO questions)", xaxis_title="Language")
st.plotly_chart(fig_compare, use_container_width=True)

st.markdown("""
This chart compares the popularity of programming languages on Stack Overflow between 2014 and 2024.  
It reveals which languages have grown — like **Python** and **Swift** — and which have declined, such as **PHP** and **Objective-C**.
""")

# ================================
# Programming Language Usage Across Industries
# ================================
st.markdown("---")
st.header("Programming Language Usage Across Different Industries")

industry_df = pd.read_csv("industry_language_usage.csv")
industries = ["Web Development", "Data Science", "Mobile Development", "Game Development", "Finance"]
cols = st.columns(len(industries))

for i, industry in enumerate(industries):
    df_industry = industry_df[(industry_df["Industry"] == industry) & (industry_df["Usage (%)"] > 0)]
    
    fig = px.bar(
        df_industry.sort_values("Usage (%)", ascending=True),
        x="Usage (%)",
        y="Language",
        orientation="h",
        color="Language",
        title=industry,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    fig.update_traces(width=0.5)
    fig.update_layout(
        showlegend=False,
        height=400,
        margin=dict(t=40, b=30),
        xaxis=dict(showgrid=True, gridwidth=0.5, gridcolor="gray", zeroline=False, ticks="outside")
    )
    
    cols[i].plotly_chart(fig, use_container_width=True)

st.markdown(" ")

st.markdown("""
This visualization shows how different sectors prioritize different programming languages.

- **Python** leads in data science and shows strong presence in finance.  
- **JavaScript** dominates web development, along with HTML and CSS.  
- **Java** and **C++** have major roles in mobile development, game development, and finance.
""")

# ================================
# Final Reflections
# ================================
st.markdown("---")
st.header("Final Reflections")

st.markdown("""
As I built this dashboard, I was struck by how dynamic the programming landscape really is.  
Languages like **Python** and **JavaScript** continue to thrive, but newer entries like **Rust** and **TypeScript** are quickly gaining ground — not just in admiration, but in practical use across industries.

One of the most fascinating insights was the **admiration gap** — the difference between what developers love and what they actually use or seek out.  
It made me think about how career decisions, industry demands, and learning curves all shape the tools we choose.

This dashboard deepened my appreciation for how data can tell a story — and how understanding that story can guide not just personal learning, but broader strategic decisions for teams and organizations.  
I hope others find these visualizations as thought-provoking and useful as I did.
""")
