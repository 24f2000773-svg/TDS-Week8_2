#!/usr/bin/env python3
# Employee performance analysis script
# Contact: 24f2000773@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (employee_performance.csv must be in same folder)
df = pd.read_csv("employee_performance.csv")

# Frequency count for Sales department
sales_count = (df["department"] == "Sales").sum()
print("Frequency count for 'Sales' department:", sales_count)

# Department distribution plot
dept_counts = df["department"].value_counts().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8,5))
dept_counts.plot(kind="bar", ax=ax)
ax.set_title("Department Distribution (Employee Counts)")
ax.set_xlabel("Department")
ax.set_ylabel("Number of Employees")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
fig.savefig("department_distribution.png")
