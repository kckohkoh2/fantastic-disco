import pandas as pd
import numpy as np
df=pd.read_excel('CorporationList.xlsx',index_col=0,sheet_name=1,header=2)
print(df[0:10])
print(df.loc[1:10])
df2=pd.read_excel('CorporationList.xlsx',index_col=0,sheet_name=1,header=2,nrows=12)
print(df2)
df3=pd.DataFrame(columns=df.columns)
for i in (df.index):
    if( '장학' in df.loc[i]['법인명'] and
       (('고등학교' in df.loc[i]['법인명']) or
        ('동창' in df.loc[i]['법인명']) or
        ('고장학' in df.loc[i]['법인명']) or
        ('고 장학' in df.loc[i]['법인명']) or
        ('여고' in df.loc[i]['법인명']) or
        ('공고' in df.loc[i]['법인명']) or
        ('중고' in df.loc[i]['법인명']) or
        ('동문' in df.loc[i]['법인명']))):
        df3.loc[i]=df.loc[i]
print(df3)
df3.to_excel("고등학교 장학재단.xlsx")