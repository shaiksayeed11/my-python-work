import time
def product(pid,pname,price,company):
    print("------product informatin-----")
    print("product id is",pid)
    print("product name is",pname)
    print("product price is",price)
    print("product company is",company)
print("----------------------------------------------")
product(111,"thar",23333333,"mahindra")
print()
product(112,"cycle",233433333,"yamaha")
product(115,"guitar",23343,"yamaha")

time.sleep(1)
print("end of an applicaiton")