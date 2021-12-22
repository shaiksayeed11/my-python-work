'''import time
def sqaure(x):
    for i in x:
        print("the sqaure of x is ",i*i)
def double(x):
    for y in x:
        time.sleep(1)
        print("the double of x is ",2*y)
x=[1,2,3,4,5]
begintime=time.time()
sqaure(x)
double(x)
endtime=time.time()
print(endtime)
'''
import time
from threading import*
def sqr(num):
    for i in num:
        time.sleep(1)
        print("the sqaure of given list of numbers are",i *i)
def double(num):
    for j in num:
        time.sleep(1)
        print("the double of given number of list are ",2*j)
num=[1,2,3,4,5]
t=Thread(target=sqr,args=num,)
t.start()
t1=Thread(target=double,args=num,)
t1.start()
