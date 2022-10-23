import pandas as pd
import numpy as np
df=pd.read_excel('list_data.xlsx',index_col=0) #0번 열을 인덱스로 지정
df.loc[6]=['윤석열',61,176.6,77.6,'B']
df2=pd.DataFrame([['오상규',58,172.3,72.5,'O']],columns=df.columns)
df=df.append(df2,ignore_index=True)
df.index=np.arange(1,len(df)+1)
print(df)
print(df.loc[4:6]['이름'])
print(type(df.loc[4:6]['이름']))
print(df.iloc[0:3,0:2])
print(type(df.iloc[0:3,0:2]))
print(df[df['신장']>170])
print(df[(df['신장']>170) & (df['나이']<60)])