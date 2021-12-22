import time
from abc import*
class db(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnet(self):
        pass
class mysql(db):
    def connect(self):
        print("connectin to mysql server  for indian customerw")
    def disconnect(self):
        print("disconnect my sql server for  indian customer")
class django(db):
    def connect(self):
        print("conent django  server to indian customers")

    def disconnect(self):
        print("disconnect diango sefver with indian customers")
db=input("enter the data base")
classname=globals()[db]
x=classname()
x.connect()
time.sleep(2)
x.disconnect()