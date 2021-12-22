'''import time
a=20
b=33
res= a if a>b else b
print(res)'''
import time
a=eval(input("enter the value of a"))
b=eval(input("enter the value of b"))
c=eval(input("enter the value of b"))

res=a if a>b and a>c else b if b>c else c
print("the maximum between ",a ,"and",b ,c,"is",res)
print()
time.sleep(1)
print("end of an application")
