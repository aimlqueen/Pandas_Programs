import pandas as pd
dic={'id':1,'fname':'nimisha','lname':'davis','age':25,'designation':'da','salary':35000}
# index : print data in particular order
a=pd.Series(dic,index=['fname','lname','id','age','salary','designation'])
print(a)
