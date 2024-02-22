# list=[1,2,3,4,5,6]

# def search(list,key):
   
#     if key in list:
#         return list.index(key)

#     else:
#         return -1
# print(search(list,9))


# def findningOrder(list):
#     return 0

# print(findningOrder([1,2,3,4,5,6,]))


# def printName():
#     print("HEllo AYAN")



# printName()



# def findningSecondOrder(list):
#     pass




# def printName(first,last):
#     print(first," ", last)


# printName('ayan','khan')
# printName("Pathan") #Error  missing 1 required positional argument: 'last'

# def my_function(*kids):
#     print(kids)
# my_function('name','shabbir', 'bohra')


# def my_function(child1, child2,child3):
#     print('The Yougest child is ', child3)
# my_function(child1="Email",child1="Email",child1="Email" )



# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")



# def my_function(**kid):
#   print("His last name is " + kid['lname'])

# my_function(fname = "Tobias", lname = "Refsnes")


def my_function(num):
    return 5*num
# print(my_function(2))
# print(my_function(5))
# print(my_function(9))



# def my_function(x, /):
#   print(x)

# my_function(3)
# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

# Example
# def my_function(x):
#   print(x)

# my_function(x = 3)



# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

# # Example
# def my_function(*, x):
#   print(x)

# my_function(x = 3)
# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:

# Example
# def my_function(x):
#   print(x)

# my_function(3)

# But when adding the *, / you will get an error if you try to send a positional argument:

# Example
# def my_function(*, x):
#   print(x)

# my_function(3) # erro 



def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)



def generateNumber(start=0, end=100,n=100):
    nums=[]
    for i in range(n):
        ele= random.randrange(star,end)


list1=[0,3,1,0,11,12]
def moveZero(list1):
    for x in list1:
        if(x==0):
            list1.remove(0)
            list1.append(0)
    
    return list1
        

print(moveZero(list1))