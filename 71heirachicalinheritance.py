import  time
class parent:
    def m1(self):
        print("this is parent class")
class child1(parent):
    def m2(self):
        print("this is 1child")

class child2(parent):
    def m3(self):
        print("this is child 2 class")
t=child1()
t.m1()
t.m2()
m=child2()
m.m3()
m.m1()
print()
time.sleep(1)
print("enf of an applicationn")
