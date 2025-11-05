#summary statistics of numerical columns in pandas dataframe
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

print("\nSummary Statistics of Numerical Columns:")
print(df.describe())

print("\nMean Salary:", df['Salary'].mean())
print("Median Age:", df['Age'].median())
print("Standard Deviation of Performance Score:", df['Performance_score'].std())
print("Minimum Salary:", df['Salary'].min())
print("Maximum Age:", df['Age'].max())
print("Sum of Salaries:", df['Salary'].sum())
print("Count of Entries in Performance Score:", df['Performance_score'].count())
print("Variance of Age:", df['Age'].var())
print("25th Percentile of Salary:", df['Salary'].quantile(0.25))
print("50th Percentile (Median) of Salary:", df['Salary'].quantile(0.50))
print("75th Percentile of Salary:", df['Salary'].quantile(0.75))
print("Correlation between Age and Salary:")
print(df['Age'].corr(df['Salary']))
print("Covariance between Age and Salary:")
print(df['Age'].cov(df['Salary']))  

