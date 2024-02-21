# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.


# myTuple=['a','b','c','d','e'];
# second=list(myTuple)
# add at index
# second[0]='z'

#  add at last
# second.append('z')
# myTuple=tuple(second)
# print(myTuple)



#  add new tuple is allow in old tuple you can add in this 
# y=("orange",)
# myTuple+=y
# print(myTuple)


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)



thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
