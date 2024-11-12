import numpy as np
import pandas as pd
s=pd.Series([1,2,3,4,5])
print(s) #If we print the values,… it index will also displayed

print(type(s)) #<class 'pandas.core.series.Series'>
#shape of array. it is 1D so it will return total no elements
print(s.shape) #(5,)
#size of array
print(s.size) #5
#dataype
print(s.dtype) #int64
