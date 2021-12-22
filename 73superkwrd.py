import time
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def m1(self):
        print("name is ",self.name)
        print(" age is",self.age)
class employee(person):
    def __init__(self,name,eid,age,esal,design,company):

        super().__init__(name,age)
        self.eid=eid
        self.esal=esal
        self.design=design
        self.company=company

    def m2(self):
        super().m1()
        print("eid is",self.eid)
        print("esal is ",self.esal)
        print("designattion is",self.design)
        print("company is",self.company)
class student(person):
    def __init__(self,name,age,rollno,subject,marks):

        super().__init__(name,age)
        self.rollno=rollno
        self.subject=subject
        self.marks=marks
    def m3(self):
        super().m1()
        print("rolll no is",self.rollno)
        print("subject is ",self.subject)
        print("marl=ks are ",self.marks)
e=employee("rahul",33,11,45000,"webdeveloper","django")
e.m2()
print()
s=student("ajay verma",12,1010,"python",455)
s.m3()
print()
time.sleep(1)
print("end of an application")