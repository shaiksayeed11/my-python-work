import time
class employe:
    company="cg"
    def __init__(self,ename,esal,eid,design):
        self.ename=ename
        self.esal=esal
        self.eid=eid
        self.design=design
    def m1(self):
        print("------employee information-----")
        print("emplouue name is",self.ename)
        print("employee esal is",self.esal)
        print("employe id is",self.eid)
        print("employe designation is",self.design)
e1=employe("bilal",2222222,22,"fullstack devrloper")
e1.m1()