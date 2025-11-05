#step-1 sample dataframe
import pandas as pd
data = {
    'Name': ['Ram', 'Shyam', 'Madhu','Anita', 'Sita', 'Gita', 'Rita', 'Mita', 'Tina', 'Arjuna', 'Karna', 'Bheem'],
    'Age': [25, 30, 35, 28, 22, 27, 32, 29, 24, 31, 33, 26],
    'City': ['Delhi', 'Mumbai', 'kolkata', 'Chennai', 'Bangalore', 'Hyderabad', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Kanpur', 'Varanasi'],
    'Salary':[50000,60000,55000,52000,58000,62000,61000,59000,53000,64000,65000,57000]
}
df = pd.DataFrame(data)
print(df) 
print("Dataset Description:")
print(df.describe(include='all'))  # include='all' to get statistics for all columns
print("\nDataset Info:")
print(df.info())
print("\nColumn Names:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("\nShape of the DataFrame:")
print(df.shape)
print("\nIndex of the DataFrame:")
print(df.index)
print("\nValues in the DataFrame:")
print(df.values)
