occured=[0]*26
college="ayankhan"
# remove reapeted 
res=''
for c in college:
    ascii=ord(c)
    index=ascii -ord('a')
    if occured[index]==0:
        occured[index]=1
        res=res+c
print(res)