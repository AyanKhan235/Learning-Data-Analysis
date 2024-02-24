import numpy as np
# arr=np.array([9,8,7,6,65,4,3,])
# print(arr)
# print(type(arr))

# arr1=np.array((1,2,3,4,5))
# print(arr1)
# print(type(arr1))


# Dimension of array 

# 0-D 
a=np.array(54)
# print(a)
print(a.ndim)
# 1-D
b=np.array([1,2,3,4])
# print(b)
print(b.ndim)


#2-D
c=np.array([[1,2,3],[4,5,6]])
print(c.ndim)
# print(c)

#3-D
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3,],[4,5,6]]])
print(d.ndim)
# print(d)


arr=np.array([1,2,3,4], ndmin=5)
print(arr)