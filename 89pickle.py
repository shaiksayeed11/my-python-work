import time
import pickle
class train:
    def __init__(self,tno,tname,arrtime,deptitme,date):
        self.tno=tno
        self.tname=tname
        self.arrtime=arrtime
        self.depttime=deptitme
        self.date=date
    def m1(self):
        print("train name is",self.tname)
        print("tno is ",self.tno)
        print("train arrtime",self.arrtime)
        print("train depttime is",self.depttime)
        print("date is ",self.date)
print("pickling process")
with open("pick.txt","wb") as f:
    t=train(1111,"hyd expess","11:30am","12:30","1/2/2020")
    pickle.dump(t,f)
    print("picling is done")
print()
with open("pick.txt","rb")as f:
    obj=pickle.load(f)
    print("unpickling is done ")

    obj.m1()


    
    