import pandas as pd

# Load the dataset
df = pd.read_csv('Dataset/customer.csv', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'designation', 'salary', 'loc']
print(df)
# drop duplicate rows
df1=df.drop_duplicates()
print(df1)
# drop columns
df2=df.drop(columns='lname')
print(df2)
# or
df3=df.drop(['lname'],axis=1)
print(df3)
