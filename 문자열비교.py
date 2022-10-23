import pandas as pd
df=pd.read_excel('list_patients.xlsx',index_col=0)
print(df)
df3=pd.DataFrame(columns=df.columns)
print(df['나이'][0])
n=0
for i in range(len(df.index)):
    if(df.loc[i]['나이']>30):
        df3.loc[n]=df.loc[i]
        n+=1
print(df3)
val_list=df.values.tolist()
col_list=list(df.columns)
index_list=list(df.index)
index_name=df.index.name
df2=pd.DataFrame(val_list,columns=col_list,index=index_list)
df2.index.name=index_name
print(df2)