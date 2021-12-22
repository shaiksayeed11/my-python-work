import time
try:
    a=int(input("enter value of a"))
    b=int(input("enter the value of b"))
    res=a//b
    print("the result is ",res)
except ZeroDivisionError :
    print("zero dicision error")
except ArithmeticError :
    print("arithmetic error")
except ValueError:
    print("value errr")

print()
time.sleep(1)
print("end of an application")