import numpy as np
arr=np.array([1,2,3,4,5,])
newarr=np.array_split(arr,3)
newarr = np.array_split(arr, 4)
newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr)