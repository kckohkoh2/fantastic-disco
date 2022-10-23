import matplotlib.pyplot as plt
import numpy as np
def f(x):
    y=1-np.exp(-x/10)
    return y
x=np.arange(1,101)
y=f(x)
plt.plot(x,y,label='output')
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.axis([0,100,0,1.2])
plt.legend(loc='upper right',ncol=1)
plt.grid(True,linestyle='--')
plt.title('Simulation Result')
plt.show()

