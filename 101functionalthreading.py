import time
from threading import*
def test():
    for x in range(5):
        time.sleep(1)
        print("child threading")
t=Thread(target=test)
t.start()
for y in range(5):
    time.sleep(1)
    print("main thread")
print()
time.sleep(1)
print("end og na application")