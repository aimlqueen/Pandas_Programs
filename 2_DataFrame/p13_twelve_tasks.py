import pandas as pd

# Load the dataset
df = pd.read_csv('Dataset/customer.csv', sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'designation', 'salary', 'loc']

# Convert age to numeric, coercing errors to handle missing values
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# 1. Extract fname, lname, age, loc
df1 = df[['fname', 'lname', 'age', 'loc']]
print(df1)

# 2. Find total number of missing values
df2 = df.isna().sum()
print(df2)

# 3. Fill missing values (loc with 'india', age with median)
df3 = df.fillna({'loc': 'india', 'age': df['age'].median()})
print(df3)

# 4. People working in India - fname, lname, age, designation
df4 = df3.loc[df3['loc'] == 'india', ['fname', 'lname', 'age', 'designation']]
print(df4)

# 5. People in India & age > 40 - fname, lname, age, designation
df5 = df3.loc[(df3['loc'] == 'india') & (df3['age'] > 40), ['fname', 'lname', 'age', 'designation']]
print(df5)

# 6. Data for people working in the US
df6 = df3.loc[df3['loc'] == 'us']
print(df6)

# 7. US work & age - max 5 employees - fname, lname, age, designation
df7 = df3.loc[df3['loc'] == 'us'].nlargest(5, 'age')[['fname', 'lname', 'age', 'designation']]
print(df7)

# 8. India work & age min 3 employees - fname, lname, age, designation
df8 = df3.loc[df3['loc'] == 'india'].nsmallest(3, 'age')[['fname', 'lname', 'age', 'designation']]
print(df8)

# 9. UK work, age range between 25-35 (inclusive)
df9 = df3.loc[(df3['age'] >= 25) & (df3['age'] <= 35) & (df3['loc'] == 'uk'), ['fname', 'lname', 'age', 'designation']]
print(df9)

# 10. Australia work, age max 1 employee - full data
df10 = df3.loc[df3['loc'] == 'australia'].nsmallest(1, 'age')
print(df10)

# 11. Pilot profession, age max 1 employee - fname, lname, age, designation
df11 = df3.loc[df3['designation'] == 'pilot'].nlargest(1, 'age')[['fname', 'lname', 'age', 'designation']]
print(df11)

# 12. US work & profession musician, age max 1 employee - full data
df12 = df3.loc[(df3['loc'] == 'us') & (df3['designation'] == 'musician')].nlargest(1, 'age')
print(df12)
