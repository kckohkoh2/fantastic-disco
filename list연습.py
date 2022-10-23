import sys
print(sys.version)
x=[1,2,3,4,5] #x는 list변수
y=[0,0,0,0,0]
for i in range(5):
    y[i]=0.5*x[i]+2
print(y,type(y))