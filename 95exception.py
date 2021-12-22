import time
try:
    a=int(input("enter the value off a"))
    b=int(input("enter the value of b"))
    res=a//b
    print(res)
except BaseException as e:
    print("there is an exceptino")
print()
time.sleep(1)
print("end of an application")