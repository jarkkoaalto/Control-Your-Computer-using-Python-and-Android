import time

print(time.time())


## Functions
def fun1():
    print("This is fun 1")

def fun2(var1,var2):
    print(var1 + var2)

fun1()
sum = fun2(10,20)

# Try catch

try:
    print("sss")
except:
    print("There is something wrong")
