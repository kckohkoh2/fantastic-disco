import pandas as pd
list_data=[['고경철',62,163.5,68.8,'B'],
           ['이주영',58,162.3,57.5,'A'],
           ['홍길동',17,188.8,88.8,'AB'],
           ['손흥민',35,180.5,82.3,'O']]
column_name=['이름','나이','신장','체중','혈액형']
index_list=[1,2,3,4]
index_name='환자번호'
print(list_data)
df1=pd.DataFrame(list_data,columns=column_name,index=index_list)
df1.index.name=index_name
print(df1)
df1.to_excel('list_data.xlsx')