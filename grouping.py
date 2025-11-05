# grouping data in pandas dataframe based on a specific column
import pandas as pd
data = {
    'Name': ['Ram', 'Shyam', 'Madhu','Anita','Joseph','Hari','Sita', 'Gita', 'Rita', 'Mita', 'Tina'],
    'Age': [25, 30, 35, 28, 30, 25, 28, 30, 35, 35,28],
    'Salary':[50000,60000,55000,52000,60000,50000,58000,62000,61000,59000,53000]
}   
print("Original DataFrame:")
df = pd.DataFrame(data)
print(df)
# grouping by single column - Age
grouped_age = df.groupby("Age")["Salary"].sum()
print("\nGrouped by Age (sum of Salary):")
print(grouped_age)
# grouping by multiple columns - Age and Name
grouped_age_name = df.groupby(["Age", "Name"])["Salary"].sum()
print("\nGrouped by Age and Name (sum of Salary):")
print(grouped_age_name)