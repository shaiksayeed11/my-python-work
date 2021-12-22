import time
class a:
    def m1(self):
        print("this is parent calssa")
class b(a):
    def m2(self):
        print("this is child class of b")
class c(b):
     def m3(self):
         print("this is child class of b")

class d(c):
    def m4(self):
        print("this is child class of c")
t=d()
t.m4()
t.m1()
t.m2()
t.m4()
t.m3()
print()
time.sleep(1)
print("end of an application")