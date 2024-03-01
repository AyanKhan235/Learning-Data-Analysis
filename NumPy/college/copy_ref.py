import numpy as np
newList=np.array([12,32,45])
#  list me slice copy krta hau or numpy me refer krta ahi 
newList2=newList[:]
newList[0]=21
print(newList)
print(newList2)