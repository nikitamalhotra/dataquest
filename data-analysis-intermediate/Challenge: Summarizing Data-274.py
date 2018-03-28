## 2. Introduction to the Data ##

import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")

all_ages.head()
recent_grads.head()

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()

for major_cat in all_ages["Major_category"].unique():
    filtered = all_ages[all_ages["Major_category"] == major_cat]
    aa_cat_counts[major_cat] = int(filtered["Total"].sum())
    
for major_cat in recent_grads["Major_category"].unique():
    filtered = recent_grads[recent_grads["Major_category"] == major_cat]
    rg_cat_counts[major_cat] = int(filtered["Total"].sum())

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0

low_wage_proportion = recent_grads["Low_wage_jobs"].sum() / recent_grads["Total"].sum()
print(low_wage_proportion)

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for major in majors:
    if recent_grads[recent_grads['Major'] == major]["Unemployment_rate"].iloc[0] < all_ages[all_ages['Major'] == major]["Unemployment_rate"].iloc[0]:
        rg_lower_count += 1

print(rg_lower_count)