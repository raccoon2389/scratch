class Mullayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self,x,y):
        self.x = x
        self.y = y
        out = x*y

        return out
    
    def backward(self,dout):
        dx = dout * self.y
        dy = dout * self.x

        return dx,dy

class Addlayer:
    def __init__(self):
        pass
    def forward(self,x,y):
        out = x+y
        return out
    def backward(self,dout):
        dx = dout*1
        dy = dout*1
        return dx,dy


apple = 100
apple_num =2
orange = 150
orange_num = 3
tax = 1.1

mul_apple_layer = Mullayer()
mul_orange_layer = Mullayer()
add_apple_orange_layer = Addlayer()
mul_tax_layer = Mullayer()

apple_price = mul_apple_layer.forward(apple,apple_num)
ornage_price = mul_orange_layer.forward(orange,orange_num)

orange_apple = add_apple_orange_layer.forward(apple_price,ornage_price)

price = mul_tax_layer.forward(orange_apple,tax)

print("순전파 : ",price)

dprice = 1
dapple_orange , dtax = mul_tax_layer.backward(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backward(dapple_orange)
dapple_num, dapple = mul_apple_layer.backward(dapple_price)
dorange_num, dorange = mul_orange_layer.backward(dorange_price)

dapplenum,dapple = mul_apple_layer.backward(dapple_price)

print(dapple,dapplenum,dorange,dorange_num,dtax)