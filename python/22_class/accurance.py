sentance="TODAY IS SOMVAR"
# sentance=sentance.upper()
# freq=[0]*26
# for c in sentance:
#     acii=ord(c)
#     index=acii-ord('A')
#     freq[index]+=1
# print(freq)
# print(chr(freq.index(max(freq))+ord('A')))

freq={}
for c in sentance:
    freq[c]=freq.get(c,0)+1
print(freq)
maximun=max(freq.values())
print(maximun)

for ele in freq:
    char=freq.get(ele, 0)
    if maximun == char:
        print(ele)
        
    



