# external data set is always 2D data
import pandas as pd
# read csv file
df=pd.read_csv('Dataset/customer.csv',sep=',',header=None)
# by default sep is comma(,)
# if no header,by default the first row will act as header
# so we've to pass header=None
df.columns=['id','fname','lname','age','designation','salary']
print(df)
print(df.head(2))
print(df.tail(2))
print(df.dtypes)
print(df.columns)
print(df.describe(include='all'))
# Ques:Calculate total no of missing values
print(df.isna().sum())

#fillna() - handling missing values
df1=df.fillna('test') # fill all missing value
print(df1)
# we'll discuss later : more handling method like col wise
















