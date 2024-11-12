import pandas as pd
df=pd.read_csv('Dataset/missing_value.csv')
print(df)
print(df.head())
print(df.tail())
print(df.columns)
print(df.dtypes)
print(df.describe(include='all'))
print(df.isna().sum())# Calculate total no of missing values
df1=df.fillna('test') # fill all missing value
print(df1)
# Ques: How to rename column in dataframe
# syntax:
# newdataframename=olddataframename.rename(columns={'oldcolname':'newcolname'})
df2=df1.rename(columns={'Max Pulse':'Maximum Pulse'})
print(df2)