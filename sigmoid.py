import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1/(1+np.exp(-10*x))
def step_function_for_numpy(x):
    y=x>0
    return y.astype(np.int)
plt.grid()
x=np.arange(-5.0,5.0,0.01)
y1=sigmoid(x)
y2=step_function_for_numpy(x)
plt.plot(x,y1,'r-',x,y2,'b--')
plt.show()
