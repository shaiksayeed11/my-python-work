import time
try:
    a=int("enter the value of a ")
    b=int("enter the value of b")
    res=a//b
    print("the result is",res)
except(ZeroDivisionError,ArithmeticError,ValueError) as e:
    print("exception is",e)
except:
    print("value error")
