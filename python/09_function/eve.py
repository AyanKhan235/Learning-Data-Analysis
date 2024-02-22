list1=[1,2,3,4,5,6,7,8,9,10,44,22,66,65]
list2=[]
list3=[]

def seprate(list,list2,list3):
    for x in list1:
        if(x%2==0):
            list2.append(x)
        else:
           list3.append(x)
seprate(list,list2,list3)
list4=list2+list3

print(list1)

# print(list2.sort())
# print(list3.sort())
# print(list4.sort())