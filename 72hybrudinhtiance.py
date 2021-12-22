import time
class a:
    def m1(self):
        print("this is parent class")
class b(a):
    pass
class c(b,a):
    pass

    pass
print("mro of a ")
print(a.mro())
print("mro of b is")
print(b.mro())
print("mro of c")
print(c.mro())
