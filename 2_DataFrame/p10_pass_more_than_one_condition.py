import pandas as pd
df=pd.read_csv('dataset/sample.txt',header=None)
df.columns=['id','fname','lname','age','phno','loc']
# print(df)
# fname,lname,age,loc
df1=df[['fname','lname','age','loc']]
# print(df1)
# age>22
df2=df.loc[df['age']>22]
# print(df2)
# # age=24 - fname,lname,phno
df3=df.loc[df['age']==24] [['fname','lname','phno']]
# print(df3)
# # chennai oc - fname,lname,age,phno
df4=df.loc[df['loc']=='chennai'] [['fname','lname','age','phno']]
# print(df4)

# pass more than one condition in loc
# newdfname=olddfname.loc[(olddfname['columnaame]condition1)&(olddfname['columnaame]condition2)]
df5=df.loc[(df['age']>24)&(df['age']<380)]
print(df5)

#
















