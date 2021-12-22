'''import time
for  i in range(10):
    print(i,end=" ")
time.sleep(1)
print("end of an applicaion")'''
'''import time
l=["apple ","banana","mango","grapes","almonds","papaya"]
for t in l:
    print(t)
print()
print(l)
time.sleep(1)
print("end of an application")'''
import time
n=eval(input("enterr number of products information"))
for i in range(n):
    pid=input("enter product id")
    pname=input("enter product name")
    price=float(input("enter the product price"))
    company=input("enter the company of product")
    for y in i:
            print(y)
print()
print("----product infromation is------")
print("product id is",pid)
print("product name is",pname)
print("product price is",price)
print("product company is",company)
print("--------------------------")
time.sleep(1)
print("end of application")