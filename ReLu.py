import numpy as np
import matplotlib.pyplot as plt
def ReLU(x):
    return np.maximum(0,x)
x=np.arange(-5.0,5.0,0.01)
y2=ReLU(x)
plt.plot(x,y2,'r-')
plt.grid()
plt.show()
