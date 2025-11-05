import pandas as pd
data = {
    'Name': ['Ram', 'Shyam', 'Madhu','Anita', 'Sita', 'Gita', 'Rita', 'Mita', 'Tina', 'Arjuna', 'Karna', 'Bheem'],
    'Age': [25, 30, 35, 28, 22, 27, 32, 29, 24, 31, 33, 26],
    'City': ['Delhi', 'Mumbai', 'kolkata', 'Chennai', 'Bangalore', 'Hyderabad', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Kanpur', 'Varanasi'],
    'Salary':[50000,60000,55000,52000,58000,62000,61000,59000,53000,64000,65000,57000],
    'Performance_score':[8.5,9.0,7.5,8.0,9.2,8.8,7.8,8.3,9.1,7.9,8.7,8.4]
}
print("Original DataFrame:")
df = pd.DataFrame(data)
print(df)
# increasing salary by 5%
df['Salary'] = df['Salary'] * 1.05
print("\nDataFrame after increasing Salary by 5%:")
print(df)
