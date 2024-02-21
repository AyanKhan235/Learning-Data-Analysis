list1=[1,2,3,4,5,1,2,3,4,1,1]
list2=[6,7,8,9,10]


# list3=list1+list2
# print(list3)


# for x in list2:
#     list1.append(x)
# print(list1)
# print(list2)


list1.extend(list2)
# print(list1)
x = list1.count(1);
print(x)
