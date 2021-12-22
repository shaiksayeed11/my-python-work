import time
import json
d={"ename":"rahul","eid":2334,"esal":344444,"comapny":"tcs"}
print("------object serialization-------")
with open("object.txt" ,"w") as f:
    obj=json.dump(d,f)
    print(obj)
time.sleep(1)
print("end of an application")


print("-----object deserialization-------")
with open("object.txt","r")as f:
    obj1=json.load(f)
    for x,y in obj1.items():
        print(x,y)
    print(obj1)