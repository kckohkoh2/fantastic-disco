import pandas as pd
data2=[['홍길동',18,188.5,72.7,'A'],
       ['이재명',59,172.4,75.9,'AB'],
       ['조영남',78,169.5,80.3,'O'],
       ['고경철',63,164.5,69.0,'B'],
       ['오상규',60,172.3,77.4,'O']] #2차원 리스트
data2.append(["조규남",60,175.3,68.8,'AB']) #기존의 list자료형의 append()함수를 추가
key=['name','age','height','체중','혈액형']
patient_no=[i for i in range(1,len(data2)+1)]
df2=pd.DataFrame(data2,columns=key,index=patient_no)
print(df2,type(df2))
print(df2['name'])
print(df2.loc[4])
print(df2.loc[4]['name'])
df2.set_index('name',inplace=True)
print(df2)
print(df2.loc['고경철'])
print(df2.loc['고경철']['age'])
df2.reset_index(inplace=True)
print(df2)
#print(df2.describe())
#print(df2.shape)