import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
# print(arr[1:5])
# print(arr[1:])
# print(arr[:5])
# print(arr[-3:-1])
# print(arr[1:5:2])
# # it goes to start to end and with 2 step
# print(arr[::2])


arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,1:4])
# from both elements, return index 2:
print(arr[0:2,2])
# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr[0:4,1:5])