import time
f=open("data1.txt","w+")
l1=["1110\n","rahul\n","344444\n","python develper\n","tcs"]
d=f.writelines(l1)
print("employee informatiomn is creaftrd in file")
f.close()
print(d)
