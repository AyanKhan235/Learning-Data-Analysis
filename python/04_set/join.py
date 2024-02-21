# Join Two Sets
# There are several ways to join two or more sets in Python.

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
set1={1,2,3,4,5}
set2={1,2,6,7,8,9}
set3=set1.union(set2)
# print(set3)


# he update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
# print(set1)

# he intersection_update() method will keep only the items that are present in both sets.

# Example
# Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.intersection(y)
x.intersection(y)

# print(x)

# output
# 
# {'apple', 'cherry', 'banana'}


# print(z)


# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

# Example
# Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

#  you can also use othervariable to store
# print(x)


w = {"apple", "banana", "cherry", True}
c = {"google", 1, "apple", 2}

q = w.symmetric_difference(c)

print(q)