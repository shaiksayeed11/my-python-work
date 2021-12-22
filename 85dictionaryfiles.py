import time
f=open("rani.txt","r+")
l1={"eid ":1,"ename":"rani","esal":34444,"designatin":"python developer","company":"tcs"}
f.writelines(l1)
d=f.read()
print(d)
print("employee informationn is created ")
f.close()
print()
print(d)
print("end off an applicafion")