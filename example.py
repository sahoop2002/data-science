import pandas as pd
data = {
    'Name': ['Ram', 'Shyam', 'Madhu','Anita', 'Sita', 'Gita', 'Rita', 'Mita', 'Tina', 'Arjuna', 'Karna', 'Bheem'],
    'Age': [25, 30, 35, 28, 22, 27, 32, 29, 24, 31, 33, 26],
    'City': ['Delhi', 'Mumbai', 'kolkata', 'Chennai', 'Bangalore', 'Hyderabad', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Kanpur', 'Varanasi'],
    'Salary':[50000,60000,55000,52000,58000,62000,61000,59000,53000,64000,65000,57000]
}

df = pd.DataFrame(data)
print("DataFrame Description:")
print(df)
print("\nPeople older than 30:")
print(df[df['Age'] > 30])
print("\nPeople with Salary greater than 60000:")
print(df[df['Salary'] > 60000])
print("\nPeople older than 30 with Salary greater than 60000:")
print(df[(df['Age'] > 30) & (df['Salary'] > 60000)])

print("\nSingle column return - Names:")
print(df['Name'])
print("\nMultiple columns return - Names and Cities:")
print(df[['Name', 'City']])

