# evaluating functions : count,sum,min,max,mean
# To do these functions,first we’ve to group it first
# syntax:
# newdf=oldf.groupby('colname') ['colname'].count()
import pandas as pd

# Load the dataset
df = pd.read_csv('Dataset/customer.csv', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'designation', 'salary', 'loc']

# Convert age and salary to numeric, coercing errors to handle missing values
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')

# each location count and sort in ascending order
df1=df.groupby('loc') ['loc'].count().sort_values()
print(df1)

df1=df.groupby('age') ['age'].sum().sort_values()
print(df1)


df1=df.groupby('age') ['age'].max().sort_values()
print(df1)

df1=df.groupby('age') ['age'].min().sort_values()
print(df1)

df1=df.groupby('age') ['age'].mean().sort_values()
print(df1)