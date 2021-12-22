import time
f=open("data1.txt","r")
d=f.readlines()
for x in d:
    print(x)

f.close()