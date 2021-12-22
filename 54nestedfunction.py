'''import time
def car():
    print("this is car ")
    def engine():
        print("this is car engine")
    engine()
car()
print("end of an application")'''
import time
def m1(name):
    print("my name is",name)
    def m2(mm,dd,yyyy):
        print("my date of birth is dob:{}/{}/{}".format(mm,dd,yyyy))
    m2(1,4,2000)
m1("raja")
time.sleep(1)
print("end of an appliction")