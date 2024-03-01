import numpy as np
# weight_kg=[81,65,97,43]
# hei=np.array(weight_kg)
# # print(np.sum(hei),np.max(hei),np.min(hei))
# # print(np.median(hei))
# print(np.argmin(hei)) # it gives us index
# print(np.min(hei))
x=np.random.randint(0,20,5)
x_mean=np.mean(x)
y=(x-x_mean)**2
y_mean=np.mean(y)
for ele in zip(x,y):
    print(ele)



