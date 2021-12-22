import time
class customer:
    def __inti__(self,cname,cid,cproduct,address,phnno):
        self.cname=cname
        self.cid=cid
        self.cproduct=cproduct
        self.address=address
        self.phnno=phnno
    def m1(self):
        print("------customer information------------")
        print("customer name is",self.cname)
        print("customerr id is",self.cid)
        print("customer profut is",self.cproduct)
        print("customer address is",self.address)
        print("customer phhno is",self.phnno)

t=customer("rAJU",222,"CYCLE","nciamabas",4444444)
t.m1()
time.sleep(1)
print("end of an application")