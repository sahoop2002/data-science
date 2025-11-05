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
# checking for missing values
print("\nChecking for missing values in each column:")
print(df.isnull())
print("\nCount of missing values in each column:")
print(df.isnull().sum())
# handling missing values by removing rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with any missing values:")
print(df_dropped)
# another way of handing missing values by removing rows with all missing values
#df.dropna(inplace=True)
#print("\nDataFrame after dropping rows with all missing values:")
#print(df)
# handling missing values by filling with a specific value
df_filled = df.fillna({
    'Name': 'Sakti',
    'Age': 28,
    'City': 'Assam',
    'Salary': 60000,
    'Performance_score': 8.9
})
print("\nDataFrame after filling missing values:")
print(df_filled)
# handling missing values by forward fill
df_ffill = df.fillna(method='ffill')
print("\nDataFrame after forward fill of missing values:")
print(df_ffill)
# handling missing values by backward fill
df_bfill = df.fillna(method='bfill')
print("\nDataFrame after backward fill of missing values:")
print(df_bfill)
# checking if there are any missing values left
print("\nChecking for missing values after handling:")
print(df_filled.isnull().sum()) 
print(df_ffill.isnull().sum())
print(df_bfill.isnull().sum())
# handling missing values by interpolation
df_interpolated = df.interpolate()
print("\nDataFrame after interpolating missing values:")
print(df_interpolated)
#linear interpolation is used by default
print("\nDataFrame after linear interpolation of missing values:")
print(df_interpolated)  
#polynomial interpolation of order 2
df_interpolated_poly = df.interpolate(method='polynomial', order=2)
print("\nDataFrame after polynomial interpolation of order 2 for missing values:")
print(df_interpolated_poly)
#time interpolation (only works if index is datetime)
df['Date'] = pd.date_range(start='2023-01-01', periods=len(df), freq='D')
df.set_index('Date', inplace=True)
df_interpolated_time = df.interpolate(method='time')
print("\nDataFrame after time interpolation of missing values:")
print(df_interpolated_time)
# resetting index
df.reset_index(inplace=True)
print("\nDataFrame after resetting index:")
print(df)   
# back to previous interpolation result for checking missing values
df_interpolated = df.interpolate()
print("\nDataFrame after interpolation:")
print(df_interpolated)
# checking for missing values after interpolation
print("\nChecking for missing values after interpolation:")
print(df_interpolated.isnull().sum())
# handling missing values by filling with mean (for numerical columns)
df_mean_filled = df.copy()
df_mean_filled['Age'].fillna(df_mean_filled['Age'].mean(), inplace=True)
df_mean_filled['Salary'].fillna(df_mean_filled['Salary'].mean(), inplace=True)
df_mean_filled['Performance_score'].fillna(df_mean_filled['Performance_score'].mean(), inplace=True)
print("\nDataFrame after filling missing numerical values with mean:")
print(df_mean_filled)
# checking for missing values after filling with mean
print("\nChecking for missing values after filling with mean:")
print(df_mean_filled.isnull().sum())    