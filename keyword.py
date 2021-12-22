import pickle
def write():
    f=open("joshna.txt","wb")
    l=[1,"rahul","djano developer"]
    pickle.dump(l,f)
write()

print("pickiling is done")
def read():
    f=open("joshna.txt","rb")
    obj= pickle.load(f)
    print(obj)
    f.close()
read()