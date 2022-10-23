import numpy as np
import matplotlib.pyplot as plt
def f(x):
    y=list()
    for i in x:
        y.append(1-np.exp(-i/10))
    return y
x=[i for i in range(101)]
r=[1 for i in range(101)]
y=f(x)
plt.plot(x,r,'--',color='r',label='refernce')
plt.plot(x,y,'-',color='b',label='output')
plt.xlabel('X-Label',labelpad=0)
plt.ylabel('Y-Label')
plt.axis([0,100,0,1.2])
plt.legend(loc='upper right',ncol=1)
plt.grid(True,linestyle='--')
plt.show()

