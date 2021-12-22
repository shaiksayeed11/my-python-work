import time
l1=[11,33,44,555,666,888]
for item in l1:
    if(item>500):
        print("dear customer you required filpkart")
        break
    print("the processing items are",item)
time.sleep(1)
print("end of an application")