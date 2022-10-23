import numpy as np
def softmax(a):
    exp_a=np.exp(a)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return y
def softmax_func(x):
    c = np.max(x)
    exp_x = np.exp(x - c)
    sum_exp_x = np.sum(exp_x)
    return exp_x / sum_exp_x
a=np.array([0.1,1000.7,0.5])
print(softmax(a))
print(np.sum(softmax(a)))
print(softmax_func(a))
print(np.sum(softmax_func(a)))