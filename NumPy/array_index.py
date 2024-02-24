import numpy as np
arr=np.array([1,4,5,6,33,88])
# print(arr[5])
# print(arr[1])

# print(arr[1]+arr[3])
arr1=np.array([[1,2,3,4,5,6],[8,7,6,5,4,3]])
# print("2nd element of 1st Row", arr1[0,1])   
# print("5th element of 2 row is ", arr1[1,4])

# Access the third element of the second array of the first array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0,1,2])

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,-1])