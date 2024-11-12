import pandas as pd
df=pd.read_csv('dataset/sample.txt',header=None)
df.columns=['id','fname','lname','age','phno','loc']
# age max 1 employee fname,lname,loc
df1=df.sort_values(by='age',ascending=False).head(1) [['fname','lname','loc']]
print(df1)
# age min 2 employee fname,lname,phone
df2=df.sort_values(by='age').head(2) [['fname','lname','phno']]
print(df2)
# chennai work, age max 1 employee
df3=df.loc[df['loc']=='chennai'].sort_values(by='age').tail(1)
print(df3)