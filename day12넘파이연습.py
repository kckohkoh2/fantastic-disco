import pandas as pd
data2=[['홍길동',18,188.5,72.7,'A'],
       ['이재명',59,172.4,75.9,'AB'],
       ['조영남',78,169.5,80.3,'O'],
       ['고경철',63,164.5,69.0,'B'],
       ['오상규',60,172.3,77.4,'O']] #2차원 리스트
#print(data2, type(data2))
key=['name','age','height','체중','혈액형']
patient_no=[i for i in range(1,len(data2)+1)]
df2=pd.DataFrame(data2,columns=key,index=patient_no)
print(df2,type(df2))
val_list=df2.values #DataFrame객체를 numpy어레이객체 변환(ndarray)
print(val_list,type(val_list))
data2=list(val_list) #ndarray객체 list객체로 변환
print(data2,type(data2))
data3=df2.values.tolist() #DataFrame에서 list객체 변환 
print(data3,type(data3))
data3.append(["조규남",60,175.3,68.8,'AB']) #기존의 list자료형의 append()함수를 추가
print(data3,type(data3))
patient_no=[i for i in range(1,len(data3)+1)]
df3=pd.DataFrame(data3,columns=key,index=patient_no)
print(df3,type(df3))