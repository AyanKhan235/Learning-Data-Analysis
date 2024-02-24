import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
arr=np.concatenate((arr1,arr2))
# print(arr)


arr3=np.array([[1,2,3],[5,6,7]])
arr4=np.array([[9,8,7],[2,3,4]])
arr=np.concatenate((arr3,arr4))
# print(arr)
# output without axix =1
# [[1 2 3]
#  [5 6 7]
#  [9 8 7]
#  [2 3 4]]
# arr=np.concatenate((arr3,arr4),axis=1)
# print(arr)

arr=np.stack((arr1,arr2),axis=1)
print(arr)
arr=np.hstack((arr1,arr2))
print(arr)
arr=np.vstack((arr1,arr2))
print(arr)
arr=np.dstack((arr1,arr2))
print(arr)