import pandas as pd
df=pd.read_excel('patients.xlsx',index_col=0)
print(df)
df3=pd.DataFrame(columns=df.columns)
df3.index.name='환자번호'
n=0
for i in range(len(df.index)):
    if(df.iloc[i]['age']>40):
        df3.loc[n]=df.iloc[i]
        n+=1
print(df3)
val_list=df3.values.tolist()
col_list=list(df3.columns)
index_list=[i for i in range(1,len(df3)+1)]
index_name=df3.index.name
df2=pd.DataFrame(val_list,columns=col_list,index=index_list)
df2.index.name=index_name
print(df2)
df2.to_excel('a2.xlsx')