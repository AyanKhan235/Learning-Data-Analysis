# Set Methods
# Python has a set of built-in methods that you can use on sets.

# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others


# x={1,2,3,4,5,6,7}
# y={11,22,33,44,55,66,77}
# # 1
# x.add(11)
# # print(x)

# z=x.copy()
# print(z)

number={1,2,3,4,5,6,7,8,9,10}
odd={1,3,5,7,9}
even={2,4,6,8,10}
print(odd.isdisjoint(even))
print(number.issuperset(odd))
print(odd.issuperset(number))
print(odd.issubset(number))