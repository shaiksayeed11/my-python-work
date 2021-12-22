import time

f=open("raab.txt","r")
print()
print("----------file information------------")
print("name of the file is",f.name)
print("mode of th e file is",f.mode)
print("whether file is readale for ",f.readable())
f.close()
