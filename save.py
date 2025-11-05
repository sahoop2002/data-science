import pandas as pd
data = {
    'Name': ['Ram', 'Shyam', 'Madhu'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'kolkata']
}

df = pd.DataFrame(data)
print(df)
# Save DataFrame to different file formats
#df.to_csv('output.csv', index=False)
#df.to_excel('output.xlsx', index=False)
#df.to_json('output.json')

