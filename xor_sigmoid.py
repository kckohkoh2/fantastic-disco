import numpy as np
import matplotlib.pyplot as plt
def step_function(x):
    y=x>0 #y=True or False
    return y.astype(int) #y= 1 or 0
def Sigmoid(x):
    return 1/(1+np.exp(-10*x))
def Perceptron(x,w):
    value=Sigmoid(np.sum(x*w))
    #value=step_function(np.sum(x*w))
    return value
def XOR(a,b):
    input1=np.array([a,b,1])
    weights1=np.array([0.4,0.5,-0.3])  #OR Gate
    weights2=np.array([-0.6,-0.5,0.7]) #NAND Gate
    weights3=np.array([0.4,0.4,-0.6])  #AND Gate
    value1=Perceptron(input1,weights1)
    value2=Perceptron(input1,weights2)
    input2=np.array([value1,value2,1])
    value=Perceptron(input2,weights3)
    return value
print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))  