import numpy as np
# arr=np.array([21,55,43,22])
# x=[True,False,False,True]
# newarr=arr[x]
# print(newarr)
arr=np.array([1,2,3,4,33,446,77,22,333,44,76,898,3224,6665,67])
new_filter=[]
# for ele in arr:
#     if ele > 33:
#         new_filter.append(True)
#     else:
#         new_filter.append(False)
# newarr=arr[new_filter]
# print(newarr)

# for ele in arr:
#     if ele%2==0:
#         new_filter.append(True)
#     else:
#         new_filter.append(False)
# newarr=arr[new_filter]
# print(newarr)
arr=np.array([1,2,3,4,5,6,22,33,44,55,66,77,88])
# new_filter=arr>33
new_filter=arr % 2==0

newarr=arr[new_filter]
print(newarr)


