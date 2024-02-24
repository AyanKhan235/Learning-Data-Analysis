# nums=[12,8,21,3,16]
# new_nums=[]
# for num in nums:
#     new_nums.append(num+1)
# print(nums)
# print(new_nums)

# new_nums=[num**2 for num in nums]
# print(new_nums)

# m=5
# k=3

# nums=[-1,-2,-3,2,0]

# count=[ num for num in nums if num >= 0 ]
# if (len(count) >= k):
#     print("yes")
# else:
#     print("no")


# list1=[5,4,4,2,2,8]
# s=min(list1)
# list1=[x-s for x in list1]
# print(list1)



# nums=[2,3,4,5,6,7]
# res=[num*2 if num%2==0 else num*3 for num in nums]
# print(res)


# def square(num):
    # return num*num
# num=gen


# def  square(num):
#     return num*num
# def mymap(fn ,lst):
#     for ele in lst:
#         yield fn(ele)

# nums=[2,3,4,5,6,7,8]
# res=map[square,nums]

# res=list(res)
# print("----------")
# for ele in res:
#     print(ele, end=" ")
# print("----------")
# for ele in res:
#     print(ele, end=" ")



list1=[0,0,0,0,0,0,0,0,0,0]
nums=7014055235
nums = map(int, list(str(nums)))

for x in nums:
    # num=list1[x]
    list1[x] +=1
print(list1)



