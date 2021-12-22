import time
class emp:
    def setid(self,ename,eid,esal,desing,company):
        self.eid=eid
        self.ename=ename
        self.esal=esal
        self.design=desing
        self.company=company
    def geteid(self):
        return self.eid ,self.ename,self.esal,self.design,self.company
e=emp()
e.setid("rahul",222,455555,"python developer","capgimeni")
print()
print("------employe inforamtion-----------")
print("eid is",e.geteid())
