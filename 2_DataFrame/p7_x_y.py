import pandas as pd
df=pd.read_csv('Dataset/customer.csv',sep=',',header=None)
df.columns=['id','fname','lname','age','designation','salary']
# in this we can seprate x,y
# y is last column ( y=salary)
# x is all other columns (x=id,fname,lname,age,designation)
x=df.iloc[:,:-1]
print(x)
y=df.iloc[:,-1:]
print(y)

