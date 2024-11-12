import pandas as pd
df=pd.read_csv('dataset/customer.csv')
df.columns=['id','fname','lname','age','designation','salary']
# df1=df[['fname','lname','age','designation']]
# print(df1)
# loc : used to filter(display data that satisify the conditions)
# ex: age>25
# syntax
# newdfname=olddfname.loc[olddfname['columnname']condition]
# df2=df.loc[df['age']>26]
# print(df2)
# collect needed cols
df2=df.loc[df['age']>26] [['fname','lname','age','designation']]
print(df2)
