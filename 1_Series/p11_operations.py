import pandas as pd
a=pd.Series([1,2,3,4,5])
b=pd.Series([6,7,8,9,10])
# add two series
c=a.add(b)
print(c)
# subtract
d=a.subtract(b)
print(d)
# multiply
e=a.multiply(b)
print(e)
# divide
f=a.divide(b)
print(f)