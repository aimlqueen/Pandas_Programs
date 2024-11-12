import pandas as pd

# Load the dataset
df = pd.read_csv('Dataset/customer.csv', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'designation', 'salary', 'loc']
# print(df)
# drop duplicate rows
df1=df.drop_duplicates()
# print(df1)
# Remove rows with duplicate 'salary', keeping the first occurrence
df_unique = df.drop_duplicates(subset='salary', keep='first')
print(df_unique)
