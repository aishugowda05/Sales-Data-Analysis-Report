import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset correctly
df_a = pd.read_csv("C:\\brainwave_matrix_task\\task1(a).csv")
df_b = pd.read_csv("C:\\brainwave_matrix_task\\task1(b).csv")

print(df_a.shape)  # Check number of rows and columns
print(df_b.shape)  # Check number of rows and columns

# Now, safely call describe()
desc_stats = df_b.describe()
print(desc_stats)

# Extract failure types and their counts
failure_types = ["TWF", "HDF", "PWF", "OSF", "RNF"]
failure_counts = df_b[failure_types].sum()

# Pie Chart - Distribution of Machine Failure types
plt.figure(figsize=(8, 6))
plt.pie(failure_counts, labels=failure_types, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
plt.title("Distribution of Machine Failure Types")
plt.show()

# Line Chart - Air Temperature Trend Over Time
plt.figure(figsize=(10, 5))
sns.lineplot(x=df_b.index, y=df_b["Air temperature [K]"], color="b")
plt.xlabel("Index")
plt.ylabel("Air Temperature (K)")
plt.title("Air Temperature Trend Over Time")
plt.show()

# Scatter Plot - Relationship between Torque and Rotational Speed
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_b["Rotational speed [rpm]"], y=df_b["Torque [Nm]"], alpha=0.5)
plt.xlabel("Rotational Speed (rpm)")
plt.ylabel("Torque (Nm)")
plt.title("Torque vs. Rotational Speed")
plt.show()

# Stacked Column Chart - Machine Failures by Type
df_b_failures = df_b[df_b["Machine failure"] == 1][failure_types].sum()
df_b_failures.plot(kind="bar", stacked=True, figsize=(8, 6), color=sns.color_palette("Set2"))
plt.ylabel("Count")
plt.title("Stacked Column Chart of Machine Failures by Type")
plt.show()

# Area Chart - Process Temperature Trends
plt.figure(figsize=(10, 5))
plt.fill_between(df_b.index, df_b["Process temperature [K]"], color="skyblue", alpha=0.4)
plt.xlabel("Index")
plt.ylabel("Process Temperature (K)")
plt.title("Process Temperature Trend Over Time")
plt.show()

desc_stats
