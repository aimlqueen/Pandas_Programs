import pandas as pd
# nested list-it's a 2D data
a=[
    [1,'nimisha','davis',25,'da',25000],
    [2,'nisa','fendro',36,'python',20000],
    [3,'mini','davis',65,'accounts',18900],
    [4,'davis','kl',71,'software tester',15000],
    [5,'shareef','vc',36,'manager',22000],
]
df=pd.DataFrame(a)
df.columns=['id','fname','lname','age','designation','salary']
# sort
# syntax:        newdf=olddf.sort_values(by='colname')
# ascending order
df1=df.sort_values(by='age')
print(df1)
# descending order
df1=df.sort_values(by='age',ascending=False)
print(df1)
