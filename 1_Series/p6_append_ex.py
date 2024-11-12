import numpy as np
import pandas as pd
a=pd.Series([1,2,3,4])
b=pd.Series([5,6,7,8])

# append
s3 = a._append(b)
print(s3)

print("-"*30)

s3 = a._append(b,ignore_index=True)
print(s3)
