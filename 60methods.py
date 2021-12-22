import time 
class product:
    def __init__(self):
        self.pid=211
        self.pname="cycle"
        self.price=22222
        self.company="infosys"
    def m1(self):
        print("product id is",self.pid)
        print("product name is",self.pname)
        print("product price is",self.price)
        print("product campnay is",self.company)
t=product()
t.__init__()
t.m1()
time.sleep(2)
print("enf of an application")