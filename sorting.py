# sorting data in pandas dataframe
# sorting data in one or more columns - there is a method called sort_values() which is used for sorting data in pandas dataframe.
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

df.sort_values(by=['Age','Salary'], ascending=False, inplace=True)
print("\n dataframe after sorting by age and salary in descending order:")
print(df)   
# sorting by single column - Age
df_sorted_age = df.sort_values(by='Age',inplace=False)
print("\nDataFrame sorted by Age:")
print(df_sorted_age)
# sorting by single column - Salary in descending order
df_sorted_salary_desc = df.sort_values(by='Salary', ascending=False,inplace=False)
print("\nDataFrame sorted by Salary in descending order:")
print(df_sorted_salary_desc)
# sorting by multiple columns - Age and Salary
df_sorted_age_salary = df.sort_values(by=['Age', 'Salary'],inplace=False)
print("\nDataFrame sorted by Age and Salary:")
print(df_sorted_age_salary)
# sorting by multiple columns - Age (ascending) and Salary (descending)
df_sorted_age_salary_mixed = df.sort_values(by=['Age', 'Salary'], ascending=[True,False],inplace=False)
print("\nDataFrame sorted by Age (ascending) and Salary (descending):")
print(df_sorted_age_salary_mixed)   
