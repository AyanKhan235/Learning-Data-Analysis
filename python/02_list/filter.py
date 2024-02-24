import math
def isOdd(num):
    print(f"isOdd((num))={num % 2}")
    return num % 2==0
num=[12,13,23,55,7]
res=filter(isOdd,num)
print(list(res))