fruits=["mango", "banana", "apple", "ab", "bango"]
# fruits.sort()
# print(fruits)
def myfun(n):
    return abs(n-50)
number=[10,30,50,23,80,100]
number.sort(key = myfun)
# print(number)


# // sort in decending
# number.sort(reverse=True)
# print(number)

# fruits.sort(key= str.upper)
# print(fruits)


fruits.reverse()
# print(fruits)



one=[1,2,3]
one=one*3
one.sort()
print(one)