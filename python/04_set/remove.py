myset={"a","b", "c", "d", "e", "f", "g"}
myset.remove("a")
print(myset)

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.
myset.pop()
print(myset)


# Example
# The clear() method empties the set:
print(myset.clear())




#  del keyword delete the full set
thisset={1,2,3,4,5,6,7,8}
del thisset
print(thisset)