# Practice 01
#
# Task: Make a simple calculator first it will ask the number then it will ask the symbol (+,-,*,/)
# then it will ask the second number and it will show us the result
#

def add(first, second):
    result = first + second
    print(result)

def sub(first, second):
    result = first - second
    print(result)

def mul(first, second):
    result = first * second
    print(result)

def div(first, second):   
    try:
        result = first / second
        print(result)
    except:
        print("can't dicided by zero")

while  True:
    first = int(input("Enter first number: "))
    firstin = input("(+,-,*,/)")
    second = int(input("enter second number:"))

    if(firstin == '+'):
        add(first, second)
    elif(firstin == '-'):
        sub(first, second)
    elif(firstin == '*'):
        mul(first, second)
    elif(firstin == '/'):
        div(first, second)
    else:
        print("Wrong only choose from the bracket")
