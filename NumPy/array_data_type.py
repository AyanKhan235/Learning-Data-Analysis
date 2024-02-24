import numpy as np
# arr=np.array([1,2,3,4,5])
# arr=np.array([1,2,3,4,5],dtype="i4")
# arr=np.array([1,2,3,4,5],dtype="i4") # error

# arr1=np.array(["apple", "mango","banana"], dtype='S')
# print(arr1.dtype)
# print(arr.dtype)


#  Covert 
arr=np.array(['1','2','3'])
newarr=arr.astype('i')  
print(arr)
print(newarr)


arr1=np.array([1.1,2.3,5.7])
newarr1=arr1.astype(int)
print(arr1)
print(newarr1)


arr2=np.array([1,2,0])
newarr2=arr2.astype(bool)
print(arr2)
print(newarr2)