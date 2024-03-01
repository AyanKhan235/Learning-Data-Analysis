import numpy as np
x=np.random.randint(0,100,20)
print(x)
bool_array= x >50  



print(bool_array)
# print(x[ x>40 and x<80])
print(x[(x>=40) & (x<=80)])