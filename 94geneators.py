'''import time
def mygen():
    yield "python"
    yield "advance python"
    yield "django with rest api"
x=mygen()
print(next(x))
print(next(x))'''
import time
def game(num):
    print("your time starts now")
    while num>10:
        num=num+1
        yield num

    print("your time is over")
x=game(0)
for i in x:
    time.sleep(1)
    print(i)

