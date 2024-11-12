import pandas as pd
a=[
    [1,'nimisha','davis',25,'da',25000],
    [2,'nisa','fendro',36,'python',20000],
    [3,'mini','davis',65,'accounts',18900],
    [4,'davis','kl',71,'software tester',15000],
    [5,'shareef','vc',36,'manager',22000],
]
df=pd.DataFrame(a)
df.columns=['id','fname','lname','age','designation','salary']
# how to collect columns
df1=df[['fname','designation']]
print(df1)
