import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
# x=np.where(arr==4)
# y=np.where(arr%2==0)
# z=np.where(arr%2==1)
# print(x)
# print(y)
# print(z)

# x=np.searchsorted(arr,6)
w=np.searchsorted(arr, 7, side="right")
arr=np.array([1,3,5,7,9])
x=np.searchsorted(arr,[2,4,6,8])
# print(x)


newarr=np.array([1,3,6,4,3,2])
print(np.sort(newarr))
new=np.array([[1,5,2],[7,4,2]])
print(np.sort(new))

booleanarray=np.array([True,False,False,True])
print(np.sort(booleanarray))