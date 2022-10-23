import numpy as np
import matplotlib.pyplot as plt
def AND(a,b):
    input=np.array([a,b])
    weights=np.array([0.4,0.4])
    bias=-0.6
    value=np.sum(input*weights)+bias
    if value<=0:
        return 0
    else:
        return 1
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))    
x1=np.arange(-2,2,0.01)
bias=-0.6
y=(-0.4*x1-bias)/0.4
plt.plot(x1,y,'r--')
plt.axvline(x=0)
plt.axhline(y=0)
plt.xlim(-0.5,1.5)
plt.ylim(-0.5,1.5)
plt.grid()
plt.show()
    