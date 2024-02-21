def functionName(parameters):
    statement(s)


def fun(a):
    print(a)

fun(6) # correct
# fun(1,2) # error
fun((3,4)) # tuple

#  accept as tuple
def newfun(*a):
    print(a)
    print(type(a))
newfun(5,6,7,8,6) 


# def new(**p):
#     print(p,)
# new(2)


# def func(b,*a):
#     print("b is ", b)
#     print("a is  tuple", a)
# print(func(1,2,3,4,5,6,7,8))

# for c in "ayanKhan":
#     print(c, ord(c))


def mysum(*a):
    total=0
    for ele in a:
        print(total, "+", ele, "=")
        total+=ele
        print(total)
    return total
# print(mysum(2,3,4,5,6))


total=mysum  # function pointer
# print(total(2,3))


# overloading
def num(a,b):
    print("first")

def num(a,b,c):
    print("ye")
num()
num(1,2)
num(1,2,3)