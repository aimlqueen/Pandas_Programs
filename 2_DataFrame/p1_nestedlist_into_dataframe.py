import pandas as pd
# nested list-it's a 2D data
a=[
    [1,'nimisha','davis',25,'da',25000],
    [2,'nisa','fendro',36,'python',20000],
    [3,'mini','davis',65,'accounts',18900],
    [4,'davis','kl',71,'software tester',15000],
    [5,'shareef','vc',36,'manager',22000],
]
# convert 2D data into DataFrame
df=pd.DataFrame(a)

# give column name
df.columns=['id','fname','lname','age','designation','salary']

# display in a table format
print(df)
print(df.head(2))#display first 2 values
print(df.tail(2))#displa last 2 values
print(df.size)# total no of elements
print(df.shape)# order
print(df.columns) #column names