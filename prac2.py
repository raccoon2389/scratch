import numpy as np

class Sigmoid :
    def __init__(self):
        self.out = None
    def forward(self,x):
        self.out = 1/(1+np.exp(-x))
        return out
    def backward(self,dout):
        return dout*self.out*(1.0-self.out)

class affaine22w
