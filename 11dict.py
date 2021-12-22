import time
d1={"pid":1111,"pname":"thaar","company":"mahhindra","price":123456777}
print(d1)
print("----------jupdating--------------------------")
d1["design"]="2020midel"
d1["email"]="thar@gmail.com"
print(d1)
print("product information")
for i in d1.items():
    print(i)

time.sleep(1)
print("end of an application")