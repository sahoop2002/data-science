#removing columns from a dataframe
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
# using drop() method to remove columns 
# df.drop(columns=['Column1', 'Column2'], inplace=True)
df.drop(columns=['Performance_score', 'City'], inplace=True)
print("\nDataFrame after removing 'Performance_score' and 'City' columns:")
print(df)  
# using del keyword to remove a column
# del df['Column_Name']
del df['Age']
print("\nDataFrame after deleting 'Age' column:")
print(df)  
# using pop() method to remove a column and return it
# removed_column = df.pop('Column_Name')
removed_salary = df.pop('Salary')
print("\nDataFrame after popping 'Salary' column:")
print(df)  
print("\nPopped 'Salary' column:")
print(removed_salary)   
# using .loc to remove columns by selecting all rows and specific columns to keep
# df = df.loc[:, ['Column1', 'Column2']]
df = df.loc[:, ['Name']]
print("\nDataFrame after selecting only 'Name' column using loc:")
print(df)
# using .iloc to remove columns by selecting all rows and specific column indices to keep
# df = df.iloc[:, [column_index1, column_index2]]
df = df.iloc[:, [0]]  # Keeping only the first column (Name)
print("\nDataFrame after selecting only 'Name' column using iloc:")
print(df)