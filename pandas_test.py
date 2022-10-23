import pandas as pd
import numpy as np
import matplotlib as plt
a=[1,2,3,5,np.nan,6,8] #리스트 
ds=pd.Series(a) #시리즈 객체를 생성
print(a,type(a))
print(ds,type(ds))
ds.to_excel('ds.xlsx')