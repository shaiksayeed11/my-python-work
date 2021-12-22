import time
l1=[44,55,666,77,88,999,22222,3333,444]
for item in l1:
    if(item>2000):
      print("dear customer you required more amount")
      break
    print("the items you can buy are",item)
else:
    print("all process items successfully loaded")