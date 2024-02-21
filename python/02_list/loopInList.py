thisList=["banana", "orange", "mango", "pinaple", "kiwi","apple"]
# for x in thisList:
#     print(x)


# for i in range(len(thisList)):
#     print(thisList[i])

# i=0
# while i < len(thisList):
#     print(thisList[i], " " , i)
    
#     i=i+1


# [print(x) for x in range(len(thisList))]
# [print(x) for x in thisList]



# myList=[]

# for x in thisList:
#     if "a" in x:
#         myList.append(x)


# print(myList)


# myList2=[]

# myList2=[x for x in thisList if "a" in  thisList]
# print(myList2)


myList3 = [x for x in thisList if x != "apple"]
# print(myList3)
myList4=[x for x in thisList]
# print(myList4)


# myList5= [x for x in range(10)]
# print(myList5)

# myList5= [x for x in range(10) if x <5]
# print(myList5)


myList6=[x.upper() for x in thisList]
# print(myList6)


myList6=[x.lower() for x in myList6]
# print(myList6)


myList6=[x.capitalize() for x in myList6]
# print(myList6)


mysame=['hello' for x in thisList]
# print(mysame)


fruits=["apple", "banana", "kiwi", "mango","watermelon"]
fr=[x if x !="banana" else "orange" for x in fruits]
print(fr)