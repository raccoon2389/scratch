import numpy as np
class RELU:
    def __init__(self):
        self.mask = None
    def forward(self,x):
        self.mask = (x<=0) # 0이하인 인덱스 Ture로 마스크
        out = x.copy()
        out[self.mask] = 0 # True로 마스크한 0 이하의 원소 0으로 바꾼다
        return out
    def backward(self):
        dout[self.mask]= 0
        dx = dout

        return dx

class Sigmoid:
    def __init__(self):
        self.x = None
    def forward(self,x):
        