import time
def decor(lang):
    def inner(name):
        if name=="python":
            print(name,"meant for genral purpose application")
        else:
            lang(name)
    return inner

@decor
def lang(name):
    print("the name of the languae is",name)
lang("python")

print(lang("python"))
time.sleep(1)
print("end of an application")