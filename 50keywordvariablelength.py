import time
def employe(**x):
    print("employe informarion")
    for a,b in x.items():
      
      print(a,"--------",b)
employe(ename="rahul",eid=222,esal=333333,designtion="data analyst")
