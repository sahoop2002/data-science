#missing values in pandas dataframe
import pandas as pd
data = {
    'Name': ['Ram', 'Shyam', 'Madhu',None, 'Sita', 'Gita', 'Rita', 'Mita', 'Tina', 'Arjuna', 'Karna', 'Bheem'],
    'Age': [25, 30, 35, None, 22, 27, 32, 29, 24, 31, 33, 26],
    'City': ['Delhi', 'Mumbai', 'kolkata', None, 'Bangalore', 'Hyderabad', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Kanpur', 'Varanasi'],
    'Salary':[50000,60000,55000,None,58000,62000,61000,59000,53000,64000,65000,57000],
    'Performance_score':[8.5,9.0,7.5,None,9.2,8.8,7.8,8.3,9.1,7.9,8.7,8.4]
}

print("Original DataFrame:")
df = pd.DataFrame(data)
print(df)
# linear, polynomial,time, index, values, nearest, zero, slinear, quadratic, cubic, spline, barycentric, krogner, pchip, akima
# checking for missing values
print("\nChecking for missing values in each column:")
print(df.isnull())
print("\nCount of missing values in each column:")
print(df.isnull().sum())
# linear interpolation is used by default
df['Age'] = df['Age'].interpolate(method='linear')
print("\nDataFrame after linear interpolation of missing values:")
print(df)
# polynomial interpolation of order 2
df['Performance_score'] = df['Performance_score'].interpolate(method='polynomial', order=2)
print("\nDataFrame after polynomial interpolation of order 2 for missing values:")
print(df)
