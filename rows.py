#head() method is used to return the first n rows of a DataFrame or Series. By default, it returns the first 5 rows.
#tail() method is used to return the last n rows of a DataFrame or Series. By default, it returns the last 5 rows.

import pandas as pd
df = pd.read_csv('/Users/pratipsahoo/Developer/pandas/sales_data_sample.csv',encoding='latin1')

print("First 10 rows of the DataFrame:")
print(df.head(10))
print("\nLast 10 rows of the DataFrame:")
print(df.tail(10))

print("First 5 rows of the DataFrame:")
print(df.head())
print("\nLast 5 rows of the DataFrame:")
print(df.tail())    



