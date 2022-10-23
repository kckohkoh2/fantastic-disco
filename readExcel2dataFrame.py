import pandas as pd
df=pd.read_excel('list_data.xlsx',index_col=0) #0번 열을 인덱스로 지정
print(len(df))
df.loc[len(df)]=['윤석열',61,176.6,77.6,'B']
print(df)
#df.to_excel('list_data2.xlsx')
print(df.loc[3]['혈액형']) #인덱스=1 데이터 프레임의 행을 출력 
print(df.iloc[2][4]) #인덱스번소 0번째 행, 2번째 컬럼
print(df.loc[4]['이름'])
print(df.iloc[3][0])
df.loc[4]['이름']='김백건'
df.loc[4]['신장']=172.2
print(df)