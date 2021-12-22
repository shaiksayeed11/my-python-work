import time
from threading import*
class test:
    def m1(self):
        for x in range(5):
            time.sleep(1)
            print("this is pareent class thread\n")
t=test()
t2=Thread(target=t.m1)
t2.start()
for y in range(5):
    time.sleep(1)
    print("this child class thread 00\n")
print()
time.sleep(1)
print("end og an applicaton")