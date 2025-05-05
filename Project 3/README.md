# Wage Comparison by Industry — Recreate & Remix

![Wage Visualization](../images/rec-rem.png)

## What is this project?

This project is part of a recreate-and-remix exercise, where I took an existing chart from [Data USA](https://datausa.io/profile/soc/software-developers#wage-ranking) and redesigned it to be more intuitive and comparative. The original ranked occupations by wage, but I wanted to help viewers understand not just who earns more, but how each role compares to the national median and across industries.

## Why did I build this?

The original chart was informative, but it lacked clarity when it came to comparing job roles side by side. I wanted to design something that would help people quickly see wage differences, not just in absolute terms but relative to the median wage. As someone interested in both tech and equity, I also wanted to highlight how different industries stack up - especially how certain fields consistently outperform others.

## How did I build it?

I used Python and Pandas to process the data and map job titles to their corresponding industries. Then I used Matplotlib to create a horizontal bar chart where each bar represents an occupation's average wage, along with a label showing its percentage difference from the overall median.

To improve readability and insight:
- I grouped jobs by industry
- Applied consistent colors to each industry
- Annotated each bar with the percentage difference
- Added a dashed line to show the median wage
- Included a custom legend explaining the color and reference line

---

### Tools Used

- Python  
- Pandas  
- Matplotlib  
- Seaborn  
---

### Data Source

- [Data USA – Software Developer Wage Rankings](https://datausa.io/profile/soc/software-developers#wage-ranking)

---

Let me know if you'd like to explore how this remix could be adapted to other datasets or turned into an interactive version!

