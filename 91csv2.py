import time
import csv
f=open("radha.csv","r")
d=csv.reader(f)
for i in d:
    print(i)
print(list(d))
