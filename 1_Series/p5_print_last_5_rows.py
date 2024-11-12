import numpy as np
import pandas as pd
a=pd.Series([i for i in range(1,51)])
# tail() : used print last 5 rows
print(a.tail())
print(a.tail(4))
