
"""
CodeAlpha Task 2: Exploratory Data Analysis (EDA)
Dataset: sample sales_data.csv (synthetic practice dataset).
Run: python analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "sales_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
print("1. Dataset shape:", df.shape)
print("\n2. First five rows:\n", df.head())
print("\n3. Data types and non-null counts:")
df.info()
print("\n4. Missing values:\n", df.isna().sum())
print("\n5. Duplicate rows:", df.duplicated().sum())
print("\n6. Numerical summary:\n", df.describe())

# Clean missing values for analysis
clean = df.copy()
clean["Region"] = clean["Region"].fillna(clean["Region"].mode()[0])
clean["Quantity"] = clean["Quantity"].fillna(clean["Quantity"].median())
clean["Unit_Price"] = clean["Unit_Price"].fillna(clean["Unit_Price"].median())
clean["Sales"] = clean["Unit_Price"] * clean["Quantity"] * (1-clean["Discount"])
clean["Date"] = pd.to_datetime(clean["Date"])

print("\n7. Sales by region:\n", clean.groupby("Region")["Sales"].sum().sort_values(ascending=False))
print("\n8. Sales by category:\n", clean.groupby("Category")["Sales"].sum().sort_values(ascending=False))
print("\n9. Monthly sales:\n", clean.set_index("Date").resample("MS")["Sales"].sum())

clean.to_csv(OUT / "cleaned_sales_data.csv", index=False)

category_sales = clean.groupby("Category")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
category_sales.plot(kind="bar", title="Total Sales by Category")
plt.ylabel("Sales")
plt.xlabel("Category")
plt.tight_layout()
plt.savefig(OUT / "sales_by_category.png", dpi=150)
plt.close()

region_sales = clean.groupby("Region")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(7,5))
region_sales.plot(kind="bar", title="Total Sales by Region")
plt.ylabel("Sales")
plt.xlabel("Region")
plt.tight_layout()
plt.savefig(OUT / "sales_by_region.png", dpi=150)
plt.close()

print("\nEDA completed. Cleaned data and charts saved in outputs/.")
