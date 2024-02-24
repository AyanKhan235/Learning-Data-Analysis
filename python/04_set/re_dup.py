
# list2=set(list1)
# list1=list(list2)
# print(list1)


list1=[1,2,3,4,6,5,4,5,6,3,1]
res=[]
for ele in list1:
    if ele not in res:
        res.append(ele)


print(res)

