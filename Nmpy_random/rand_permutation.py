# shuffle mean changing arrangement in array itself
from numpy import random
import numpy as np 
arr=np.array([1,3,5,6])
random.shuffle(arr)
print(arr)
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).
random.permutation(arr)
print(arr)
