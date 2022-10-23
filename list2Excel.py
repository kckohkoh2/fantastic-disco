import pandas as pd
#2차원 리스트: 리스트를 리스트로 하는 자료형
data2=[['홍길동',18,188.5,72.7,'A'],
       ['이재명',59,172.4,75.9,'AB'],
       ['조영남',78,169.5,80.3,'O'],
       ['고경철',63,164.5,69.0,'B']] 
key=['name','age','height','체중','혈액형']
patient_no=[i for i in range(1,len(data2)+1)] #['1','2','3','4']
#이름순 정렬
#평균나이, 몸무게 산포, 통계적 property 
# 리스트(파이썬자료형)->판다스 객체(DataFrame)
df2=pd.DataFrame(data2,columns=key,index=patient_no)
df2.index.name="환자번호"
print(df2)
df2.to_excel('patients.xlsx')
