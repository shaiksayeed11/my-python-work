import time
from abc import*
class vechile(ABC):
    @abstractmethod
    def m1(self):
        pass
class bike(vechile):
    def m1(sefl):
        return 2
class car(vechile):
    def m1(self):
        return "4"

class auto(vechile):
    def m1(self):
        return "3"
c=auto()
print(c.m1())
