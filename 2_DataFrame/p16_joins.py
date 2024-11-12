import pandas as pd

# Sample DataFrame 1: Employee Information
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'fname': ['Alice', 'Bob', 'Charlie', 'David'],
    'loc': ['US', 'UK', 'US', 'AU']
})

# Sample DataFrame 2: Salary Information
df2 = pd.DataFrame({
    'id': [1, 2, 3, 5],
    'salary': [70000, 80000, 60000, 90000]
})

# inner join
inner_join = pd.merge(df1, df2, on='id', how='inner')
print("Inner Join:")
print(inner_join)
# outer join
outer_join = pd.merge(df1, df2, on='id', how='outer')
print("\nOuter Join:")
print(outer_join)

# left join
left_join = pd.merge(df1, df2, on='id', how='left')
print("\nLeft Join:")
print(left_join)

# right join
right_join = pd.merge(df1, df2, on='id', how='right')
print("\nRight Join:")
print(right_join)
