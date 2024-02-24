import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# x=arr.copy() # if we change no change in copy array only changable in real array
# arr[0]=42
# print(x)
# print(arr)


# arr1=np.array([9,8,7,6,5,4,3,2,1])
# y=arr1.view() # changle in both array if we change in original array

# arr1[0]=0
# y[1]=100
# print(arr1)
# print(y)


# own its data or not
arr=np.array([1,2,3,4,5,6])
x=arr.copy() # none 
y=arr.view() # arra print   
print(x.base)
print(y.base)