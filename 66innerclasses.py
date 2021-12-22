'''import time
class car:
    print("this is car ")
    class engine:
        print("this is car engine")
        def m1(self):
            print("this instance methos of enigne")

t=car()
e=t.engine()
e.m1()
print()
time.sleep(1)
print("end of an application")'''
import time
class emp:
    def __init__(self):
        self.name="tahul"
        self.dob=self.DOB()
    def m1(self):
        print("emplye nameis",self.name)
        self.dob.m2()
    class DOB:
        def __init__(self):
            self.dd=11
            self.mm=4
            self.yy=8888
        def m2(self):
            print("employr dob is {}/{}/{}".format(self.dd,self.mm,self.yy))
e=emp()
e.m1()
t=e.DOB()
