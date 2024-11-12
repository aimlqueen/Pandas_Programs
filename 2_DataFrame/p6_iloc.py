import pandas as pd
df=pd.read_csv('Dataset/customer.csv',sep=',',header=None)
df.columns=['id','fname','lname','age','designation','salary']
print(df)
# head(): first 5 rows
# tail(): last 5 rows
#Ques: collect in between rows
df1=df.iloc[2] # 2 is the index position
print(df1)
df2=df.iloc[1:4]
print(df2)

df3=df.iloc[:,2:4] #: means complete row  , 2:4(lname,age) cols
print(df3)
