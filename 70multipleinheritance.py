import time
class p:
    def m1(self):
        print("this is instance methodd of class p or parent clas")
class p1:
    def m2(self):
        print("this is intance method of class two")
class p3:
    def m3(self):
        print("this is instance method of class p3")
class p4:
    def m4(self):
        print("this is class method of p4")
class m(p,p1,p4,p3):
    def m5(self):
        print("this is child class of p,p2,p4,p1")
t=m()
t.m1()
t.m2()
t.m3()
t.m4()
t.m5()
time.sleep(1)
print("end of anapplication")