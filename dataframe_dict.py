import pandas as pd
dict_data={'name':['고경철','홍길동','이재명','윤석열'],'age':[62,16,58,61]}
print(dict_data,type(dict_data))
df=pd.DataFrame(dict_data) #dict형 자료를 data frame으로 변환 
print(df)
print(type(df))
df.to_excel("df_data.xlsx")