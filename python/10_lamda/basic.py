# x = lambda a : a+10
# print(x(5))


# mul= lambda a, b : a*b
# print(mul(2,3))

# add=lambda a, b, c: a+b+c
# print(add(1,2,7))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

# print(mydoubler(11))


def mylamba(n):
    return lambda a: a*n

mydoubler=mylamba(2)
mytripler=mylamba(3)
print(mydoubler(11))
print(mydoubler(11))