def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b


print("Arithmetic Operations")
print("Enter the number")
a=int(input("Value of a"))
b=int(input("value of b"))
print("1 add, 2=sub, 3=mul, 4=div, 5=mod")
ch = int(input())
if ch==1:
    calculate=add
elif ch==2:
    calculate=sub
elif ch==3:
    calculate=mul
elif ch==4:
    calculate=div
else:
    calculate=mod

res=calculate(a,b)
print(res)
