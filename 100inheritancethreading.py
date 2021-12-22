import time
from threading import*
class mythread(Thread):
   def run(self):
       for x  in range(10):
           time.sleep(1)
           print("child thread one")
t=mythread()
t.start()
for y in range(10):
    time.sleep(1)
    print("parent thread one")
time.sleep(1)
print("enf of an application")