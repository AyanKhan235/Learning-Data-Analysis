# def fun(a,b,c):
#     print("value of a", a)
#     print("value of b", b)
#     print("value of c", c)
# fun(c=10,a=15,b=5)
#  a will in a whether not depedn on function and parameter position
def add(a=0,b=0):
    print("a is ", a, "b is", b)
add()
add(4)
add(5,8)

add(b=6)  # b=6 a=0

# add(a=8,4) # error 
add(a=9, b=2)

