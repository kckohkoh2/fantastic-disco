def f(c):
    c[0]=0
import numpy as np
a=np.array([1,5,3,12,45,23,78,32,9,95])
b=a
print(b,type(b))
a[1]=15
print(b,type(b))
f(a)
print(b,type(b))
