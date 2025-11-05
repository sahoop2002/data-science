#adding columns to a dataframe
import pandas as pd
data = {
    'Name': ['Ram', 'Shyam', 'Madhu','Anita', 'Sita', 'Gita', 'Rita', 'Mita', 'Tina', 'Arjuna', 'Karna', 'Bheem'],
    'Age': [25, 30, 35, 28, 22, 27, 32, 29, 24, 31, 33, 26],
    'City': ['Delhi', 'Mumbai', 'kolkata', 'Chennai', 'Bangalore', 'Hyderabad', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Kanpur', 'Varanasi'],
    'Salary':[50000,60000,55000,52000,58000,62000,61000,59000,53000,64000,65000,57000],
    'Performance_score':[8.5,9.0,7.5,8.0,9.2,8.8,7.8,8.3,9.1,7.9,8.7,8.4]
}
df = pd.DataFrame(data) 
# square bracket --- df["New_Column"] = some_data
df['Bonus'] = df['Salary'] * 0.1  # Adding a new column 'Bonus' which is 10% of 'Salary'
# using .loc[] --- df.loc[:, 'New_Column'] = some_data
df.loc[:, 'Tax'] = df['Salary'] * 0.2  # Adding a new column 'Tax' which is 20% of 'Salary'
print(df)   
# Display only the new columns to verify
print("\nNew Columns Added:")
print(df[['Bonus', 'Tax']]) 
# using insert method --- df.insert(loc, 'New_Column', some_data)
df.insert(2, 'Employee ID', ['E001', 'E002', 'E003', 'E004', 'E005', 'E006', 'E007', 'E008', 'E009', 'E010', 'E011', 'E012'])  # Inserting 'Employee ID' at index 2
print("\nDataFrame after inserting  'Employee ID' column:")
print(df)