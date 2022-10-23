import numpy as np
import matplotlib.pyplot as plt
def tanh(x):
    x=10*x
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
x=np.arange(-5.0,5.0,0.01)
y2=tanh(x)
plt.plot(x,y2,'r-')
plt.grid()
plt.show()
