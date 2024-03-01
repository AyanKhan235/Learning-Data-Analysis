import numpy as np
# print(np.arange(1,10))
# print(np.arange(25,40))
# print(np.arange(25,10,-1))

# print(np.arange(10,step=3))
# 50 element print
print(np.linspace(0,20))
print(np.linspace(1,50))
print(np.linspace(1,50, num=20))
print(np.linspace(1,100, 3))
x=np.linspace(1,100, 3)
print(type(x))
print(x.ndim)
print(x.size)
print(x.shape)
print(x.dtype)