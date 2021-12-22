import time
from threading import*
print("current thread name is",current_thread().getName)
current_thread().setName("bilal threading")
print("current thread name is",current_thread().getName)
