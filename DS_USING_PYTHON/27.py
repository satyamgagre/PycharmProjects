import pandas as pd
import matplotlib.pyplot as plt

# Employee Salary Dataset
data = {
    "Employee_ID": range(1, 16),
    "Name": ["Amit", "Sneha", "Ravi", "Priya", "Karan",
             "Neha", "Vikram", "Anita", "Suresh", "Meera",
             "Rahul", "Pooja", "Arjun", "Nisha", "Raj"],
    "Department": ["HR", "IT", "Finance", "Marketing", "IT",
                   "Finance", "HR", "IT", "Finance", "Marketing",
                   "HR", "IT", "Finance", "Marketing", "HR"],
    "Salary": [30000, 55000, 45000, 40000, 60000,
               48000, 35000, 70000, 50000, 42000,
               38000, 80000, 47000, 52000, 36000]
}

df = pd.DataFrame(data)

# Extract salary column
salary = df["Salary"]

# 📌 Range → Difference between maximum and minimum salary
data_range = salary.max() - salary.min()

# 📌 Variance → Average of squared differences from mean (measures spread)
variance = salary.var()

# 📌 Standard Deviation → Square root of variance (average deviation from mean)
std_dev = salary.std()

# 📌 Interquartile Range (IQR) → Spread of the middle 50% of salaries (Q3 - Q1)
Q1 = salary.quantile(0.25)  # 25th percentile
Q3 = salary.quantile(0.75)  # 75th percentile
IQR = Q3 - Q1

# Print results
print("Range :", data_range)
print("Variance :", variance)
print("Standard Deviation :", std_dev)
print("Interquartile Range (IQR) :", IQR)

# 📌 Histogram → Shows salary distribution
plt.hist(df["Salary"], bins=8, edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# 📌 Boxplot → Shows median, IQR, min, max, outliers
plt.boxplot(df["Salary"])
plt.title("Salary Spread (Boxplot)")
plt.ylabel("Salary")
plt.show()