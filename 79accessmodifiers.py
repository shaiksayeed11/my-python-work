import time
class  test:
    name="rooba"
    _nam1="django"
    __nam2="angular js"
    def m1(self):
        print(test.name)
        print(test._nam1)
        print(test.__nam2)
t=test()
t.m1()
print()
print(test.name)
print(test._nam1)
print(test.__nam2)
time.sleep(1)
print("end og an applications")