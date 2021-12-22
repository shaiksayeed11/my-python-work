'''import time
class test2:
    @classmethod
    def m1(cls):
        print("this is classmethod")
a=test2()
a.m1()
time.sleep(2)
print("end of an application")'''
import time
class test:
    @staticmethod
    def m1():
        print("this is static method")
t=test()
t.m1()
t.m1()
test.m1()