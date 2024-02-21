thislist=["banana", "mango", "kiwi", " orange"]
thislist.remove("banana")
print(thislist)


#  remove index wise
thislist.pop(1)
print(thislist)



#  remove last item
thislist.pop()
print(thislist)

del thislist[0]
print(thislist)


thisList=["bana", "mango", "orange", "kiwi"]
#  delete Entire List
del thisList
#this will cause an error because you have succsesfully deleted "thislist".
# print(thisList)


myList=["a", "b", "c", "d", "e"]
# / clear the full list
myList.clear();
print(myList)
