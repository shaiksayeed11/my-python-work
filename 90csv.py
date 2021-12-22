import time
import csv
with open("radha.csv","w",newline="")as f:
    d=csv.writer(f)
    d.writerow(["pid","pname","price","company","mdate","expdate"])
    n=int(input("enter the number of cloums"))
    for x in range(n):
        pid=int(input("enter the pid value"))
        pname =input("enter pname")
        price=eval(input("enter the price"))
        company=input("enter the company")
        mdate=eval(input("enter the manufacture date"))
        expdate=eval(input("enter the expadate"))
        d.writerow([pid,pname,price,company,mdate,expdate])
    print("data is stored successfully")
time.sleep(1)
print("end og an application")  