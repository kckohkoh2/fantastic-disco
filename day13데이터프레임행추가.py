import posixpath
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
df2.loc[len(df2)+1]=['심성화',58,192.3,82.5,'A'] #직접 DataFrame에서 행추가 
df3=pd.DataFrame([['문전일',55,174.6,82.3,'B'],
                  ['손흥민',33,193.5,78.8,'O']],columns=key) #한행 데이터라도 2중리스트로 해야 
print(df3)
df4=df2.append(df3,ignore_index=True) #df2의 데이터프레임에 df3의 데이터프레임을 추가 
print(df4)
pos=['의적','정치인','가수','교수','대표','언론인','회사원','원장','선수']
df4.insert(2,'직업',pos)
print(df4)
#df4.drop(4,axis=0,inplace=True)
#print(df4)
df4.drop('직업',axis=1,inplace=True)
print(df4)
df4.loc[5]=['조영남',78,169.5,80.3,'B']
print(df4)
print(len(df4))
df4.index=[i for i in range(1,len(df4)+1)]
print(df4)
print(df4[(df4['height']>170) & (df4['age']>=60)])