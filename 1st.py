import pandas as pd

# read data from a CSV file into a DataFrame
df = pd.read_csv('/Users/pratipsahoo/Developer/pandas/sales_data_sample.csv',encoding='latin1')

# read data from an Excel file into a DataFrame
df = pd.read_excel("/Users/pratipsahoo/Developer/pandas/SampleSuperstore.xlsx")

# read data from a JSON file into a DataFrame
df = pd.read_json("/Users/pratipsahoo/Developer/pandas/sample_Data.json")

print(df)

# if I store my data in cloud and want to read it directly from there for that we can use this library "gcsfs"

