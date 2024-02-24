import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# for x in arr:
#     # print(x)
# for x in np.nditer(arr):
#     print(x)
# for x in np.nditer(arr, flags=["buffered"],op_dtypes=['S']):
#     print(x)

# arr1=np.array([[1,2,3],[4,5,6]])
# for x in arr1:
#     for y in x:
#         # print(y)

# arr2=np.array([[[1,2,3],[7,8,9]],[[5,4,3],[3,4,5]]])
# for x in arr2:
#     print(x)


# for x in arr2:
#     for y in x:
#         for z in y:
#             print(z)


#  skiping 1 ele
# for x in np.nditer(arr2[:,::2]):
#     print(x)


arr = np.array([1, 2, 3])
arr=np.array([[1,2,3],[5,6,7]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)