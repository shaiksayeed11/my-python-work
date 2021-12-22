import time
class destructor:
    def __init__(self):
        print("this is constructo used to declare the variable")
    def  __del__(self):
        print("this is destructor usef to delete the objects")
t=destructor()
q=t
p=q
del t
print()
time.sleep(1)
print("end of an application")