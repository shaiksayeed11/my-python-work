import time
l1=[x*x for x in range(10) if(x%2==0)]
print("the square of number upto range 10",l1)
for o in l1:
    print(o)
print()
time.sleep(1)
print("end of an application")