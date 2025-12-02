import pandas as pd
import matplotlib.pyplot as plt

# Load employee data
df = pd.read_csv("employee_performance.csv")

# Frequency count for Sales department
sales_count = (df["department"] == "Sales").sum()
print(sales_count)

# Histogram / bar chart for department distribution
plt.figure(figsize=(8,5))
df["department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.tight_layout()
plt.savefig("department_distribution.png")
plt.close()
