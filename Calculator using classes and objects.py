
class calculator:
    def __init__(self,a,b):
        self.a=a    
        self.b=b
    def add(self):
        print("add is :",self.a+self.b)
    def sub(self):
        print("sub is :",self.a-self.b)
    def mul(self):
        print("mul is :",self.a*self.b)
    def div(self):
        print("div is :",self.a/self.b)

a=int(input("enter the value of A :"))
b=int(input("enter the value of B :"))
cal=calculator(a,b)

operation=input("enter the operation that need to perform 'add' 'sub' 'mul' 'div' :")

if(operation == "add"):
    cal.add()
elif(operation == "sub"):
    cal.sub()
elif(operation == "mul"):
    cal.mul()
elif(operation == "div"):
    cal.div()
else:
    print("invalid operation entered")


