# CodeAlpha Task 2 — Exploratory Data Analysis (EDA)

## Objective
Explore a sales dataset, inspect its structure and data quality, clean missing values, and identify sales patterns.

## Dataset
`data/sales_data.csv` is a **synthetic practice dataset created for this project**. It contains order date, region, product category, product, unit price, quantity, discount and sales. A few missing values are intentionally included to demonstrate data-quality checks.

## Questions explored
- What are the dataset dimensions and data types?
- Are there missing or duplicate records?
- Which product category and region have the highest total sales?
- How do sales change over time?

## Methods
Pandas is used for inspection, missing-value handling, summary statistics and grouping. Matplotlib creates charts. Missing region values are filled with the mode; missing numeric values are filled with the median; sales are recalculated after cleaning.

## Run
```bash
pip install -r requirements.txt
python analysis.py
```
Outputs are saved in `outputs/`.

## Limitations
Because the dataset is synthetic, the findings demonstrate an analysis workflow and should not be presented as actual company sales results.
