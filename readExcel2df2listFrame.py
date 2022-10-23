from tracemalloc import Trace
import pandas as pd
df=pd.read_excel('list_data.xlsx',index_col=0) #0번 열을 인덱스로 지정
print(len(df))
df.loc[len(df)+1]=['윤석열',61,176.6,77.6,'B']
col_list=df.columns.to_list()
df2=pd.DataFrame([['오상규',58,172.3,72.5,'O']],columns=col_list,index=[7])
df=df.append(df2)
print(df)
val_list=df.values.tolist()
val_list.append(['오상규',58,172.3,72.5,'O'])
print(val_list)
index_list=df.index.to_list()
index_list.append(len(df)+1)
df3=pd.DataFrame(val_list,columns=col_list,index=index_list)
df.drop(['7'],inplace=True)
print(df)