#pd.merge(df1,df2, on = "column_name", how = "type of join")
"""inner join: It returns only the rows with matching values in both DataFrames.
   outer join: It returns all rows from both DataFrames, filling in NaN for missing matches.
   left join: It returns all rows from the left DataFrame and matching rows from the right DataFrame.
   right join: It returns all rows from the right DataFrame and matching rows from the left DataFrame.
"""
import pandas as pd
#customers dataframe
data1 = {
    'CustomerID': [1, 2, 3, 4, 5],
    'CustomerName': ['Ram', 'Shyam', 'Madhu', 'Sita', 'Gita']
}
df_customers = pd.DataFrame(data1)  
#orders dataframe
data2 = {
    'OrderID': [101, 102, 103, 104, 105],
    'CustomerID': [1, 2, 2, 4, 6],
    'OrderAmount': [250, 450, 300, 150, 500]
}
df_orders = pd.DataFrame(data2)  


print("Customers DataFrame:")
print(df_customers)

print("\nOrders DataFrame:")
print(df_orders)
#inner join
df_inner = pd.merge(df_customers, df_orders, on='CustomerID', how='inner')
print("\nInner Join Result:")
print(df_inner)
#outer join
df_outer = pd.merge(df_customers, df_orders, on='CustomerID', how='outer')
print("\nOuter Join Result:")
print(df_outer)
#left join
df_left = pd.merge(df_customers, df_orders, on='CustomerID', how='left')
print("\nLeft Join Result:")
print(df_left)
#right join
df_right = pd.merge(df_customers, df_orders, on='CustomerID', how='right')
print("\nRight Join Result:")
print(df_right)

#joining dataframes using join() method
# set CustomerID as index for both dataframes
df_customers.set_index('CustomerID', inplace=True)
df_orders.set_index('CustomerID', inplace=True) 
# join dataframes
df_joined = df_customers.join(df_orders, how='inner')
print("\nJoined DataFrame using join() method:")
print(df_joined)
#reset index to default
df_customers.reset_index(inplace=True)
df_orders.reset_index(inplace=True)
#concatenating dataframes
data3 = {
    'CustomerID': [6, 7],
    'CustomerName': ['Rita', 'Mita']
}
df_new_customers = pd.DataFrame(data3)  
print("\nNew Customers DataFrame:")
print(df_new_customers)
# concatenate dataframes
df_concatenated = pd.concat([df_customers, df_new_customers], ignore_index=True)
print("\nConcatenated DataFrame:")
print(df_concatenated)
#appending dataframes
data4 = {
    'CustomerID': [8],
    'CustomerName': ['Tina']
}
df_another_customer = pd.DataFrame(data4)  
print("\nAnother Customer DataFrame:")
print(df_another_customer)
# append dataframe
df_appended = df_customers._append(df_another_customer, ignore_index=True)
print("\nAppended DataFrame:")
print(df_appended)
# cross join
df_cross = df_customers.merge(df_orders, how='cross')
print("\nCross Join Result:")
print(df_cross)
# merging dataframes with suffixes to handle overlapping column names
data5 = {
    'CustomerID': [1, 2, 3],
    'CustomerName': ['Ram', 'Shyam', 'Madhu']
}
df_customers1 = pd.DataFrame(data5)  
data6 = {
    'CustomerID': [2, 3, 4],
    'CustomerName': ['Sita', 'Gita', 'Rita']
}
df_customers2 = pd.DataFrame(data6)  
print("\nCustomers1 DataFrame:")
print(df_customers1)
print("\nCustomers2 DataFrame:")
print(df_customers2)
# merge with suffixes
df_merged_suffixes = pd.merge(df_customers1, df_customers2, on='CustomerID', how='inner', suffixes=('_left', '_right'))
print("\nMerged DataFrame with Suffixes:")
print(df_merged_suffixes)   
# merging dataframes using indicator to show the source of each row
df_merged_indicator = pd.merge(df_customers1, df_customers2, on='CustomerID', how='outer', indicator=True)
print("\nMerged DataFrame with Indicator:")
print(df_merged_indicator)
# merging dataframes on multiple columns
data7 = {
    'CustomerID': [1, 2, 3],
    'OrderID': [101, 102, 103],
    'CustomerName': ['Ram', 'Shyam', 'Madhu']
}
df_customers_multi = pd.DataFrame(data7)  
data8 = {
    'CustomerID': [2, 3, 4],
    'OrderID': [102, 104, 105],
    'OrderAmount': [450, 300, 500]
}
df_orders_multi = pd.DataFrame(data8)  
print("\nCustomers Multi DataFrame:")   
print(df_customers_multi)
print("\nOrders Multi DataFrame:")
print(df_orders_multi)
# merge on multiple columns
df_merged_multi = pd.merge(df_customers_multi, df_orders_multi, on=['CustomerID', 'OrderID'], how='inner')
print("\nMerged DataFrame on Multiple Columns:")
print(df_merged_multi)  
# merging dataframes with different column names
data9 = {
    'CustID': [1, 2, 3],
    'CustomerName': ['Ram', 'Shyam', 'Madhu']
}
df_customers_diff = pd.DataFrame(data9)  
data10 = {
    'CustomerID': [2, 3, 4],
    'OrderAmount': [450, 300, 500]
}
df_orders_diff = pd.DataFrame(data10)  
print("\nCustomers Different Column Names DataFrame:")
print(df_customers_diff)
print("\nOrders Different Column Names DataFrame:")
print(df_orders_diff)
# merge with different column names
df_merged_diff = pd.merge(df_customers_diff, df_orders_diff, left_on='CustID', right_on='CustomerID', how='inner')
print("\nMerged DataFrame with Different Column Names:")
print(df_merged_diff)   