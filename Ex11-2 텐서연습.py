import numpy as np
a=np.array([1,2,3])
b=np.array([[4,3,3],[2,7,2],[9,1,1]])
c=np.array([[[4,3,3],[2,7,2],[9,1,1]],
           [[2,3,9],[4,7,2],[9,8,1]],
           [[4,13,3],[2,17,2],[9,100,1]]])
print(np.ndim(a))
print(np.ndim(b))
print(np.ndim(c))
print(a.ndim)
print(b.ndim)
print(c.ndim)
d=np.linalg.inv(b)
e=np.matmul(b,d)
print(d)
print(e)