import pandas as pd
import numpy as np
a=np.arange(10,22).reshape(3,4)
print(a,type(a))
df=pd.DataFrame(a,index=[1,2,3],columns=['a','b','c','d'])
print(df)