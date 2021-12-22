import time
with open("data1.txt","r") as f:
    print("----------file information----------")
    print("name of the file is ",f.name)
    print("mode of the file is",f.mode)
    print("whehter file is closed",f.closed)
    print("file is readable ",f.readable())
    print("file is writable ",f.writable())
print("file is clooseed",f.closed)