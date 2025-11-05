#updating file to include examples of head() and tail() methods
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
# .loc[] method to update specific values
# df.loc[df['column_name] == 'row_index_name', 'column_name'] = 'new_value'
df = pd.DataFrame(data)
# Updating 'City' for 'Madhu' to 'Kolkata'
df.loc[df['Name'] == 'Madhu', 'City'] = 'Kerala'
# Updating 'Salary' for 'Sita' to 60000
df.loc[df['Name'] == 'Sita', 'Salary'] = 60000
print("\nDataFrame after updates:")
print(df)  

#another way to update using index 
# df.loc[row_index, 'column_name'] = new_value
df.loc[2, 'Age'] = 36  # Updating age of the third person (index 2) to 36
print("\nDataFrame after updating age at index 2:")
print(df)
# Using .at[] method to update a single value
# df.at[row_index, 'column_name'] = new_value
df.at[0, 'Performance_score'] = 9.0  # Updating Performance_score for the first person (index 0) to 9.0
print("\nDataFrame after updating Performance_score at index 0:")
print(df)   
# Using .iloc[] method to update by integer location
# df.iloc[row_index, column_index] = new_value
df.iloc[1, 2] = 'Chandigarh'  # Updating 'City' for the second person (index 1) to 'Chandigarh'
print("\nDataFrame after updating City at index 1 using iloc:")
print(df)
# Using .replace() method to update values
# df['column_name'] = df['column_name'].replace(old_value, new_value)
df['City'] = df['City'].replace('Delhi', 'New Delhi')  # Replacing 'Delhi' with 'New Delhi' in 'City' column
print("\nDataFrame after replacing City 'Delhi' with 'New Delhi':")
print(df)   
# Using .update() method to update values from another DataFrame
df_update = pd.DataFrame({
    'Name': ['Gita', 'Rita'],
    'Salary': [63000, 62000]
})
df.set_index('Name', inplace=True)
df_update.set_index('Name', inplace=True)
df.update(df_update)
df.reset_index(inplace=True)
print("\nDataFrame after updating Salary from another DataFrame:")
print(df)   
# Using .where() method to conditionally update values
df['Salary'] = df['Salary'].where(df['Salary'] <= 60000, 60000)  # Setting Salary to 60000 if it is greater than 60000
print("\nDataFrame after conditionally updating Salary using where():")
print(df)       
# Using .mask() method to conditionally update values
df['Age'] = df['Age'].mask(df['Age'] < 25, 25)  # Setting Age to 25 if it is less than 25
print("\nDataFrame after conditionally updating Age using mask():")
print(df)   
# Using .assign() method to create a new column with updated values
df = df.assign(Experience=lambda x: x['Age'] - 22)  # Adding a new column 'Experience' based on 'Age'
print("\nDataFrame after adding 'Experience' column using assign():")
print(df)
# Using .apply() method to update values based on a function
df['Salary'] = df['Salary'].apply(lambda x: x * 1.05)  # Increasing Salary by 5%
print("\nDataFrame after updating Salary using apply():")
print(df)
# Using .fillna() method to update NaN values
df.loc[3, 'City'] = None  # Introducing a NaN value for demonstration
df['City'] = df['City'].fillna('Unknown')  # Filling NaN values with 'Unknown'
print("\nDataFrame after filling NaN values in City using fillna():")
print(df)
