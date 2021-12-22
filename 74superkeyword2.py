'''import time
class parent:
    def __init__(self):
        print("its a construtor method of parent class")
        print("constructor is used to initialise the varilabels")
    def m1(self):
        print("this isnstance merthod of parent class ")
        print("instance method is used to write businesslogic")
    @classmethod
    def m3(cls):
        print("this is class method ")
    @staticmethod
    def m4():
        print("this is stat ic method of parent clwass")

class child(parent):
    def __init__(self) :
        super().__init__()
        super().m1()
        
        super().m3()
        super().m4()
c=child()'''
import time
class python:
    nam1="advanve python"
    def __init__(self):
        self.name2="amgular js"
class django(python):
    def m2(self):
        print("name is",super().nam1)
        print("name 2",self.name2)
d=django()
d.m2()
