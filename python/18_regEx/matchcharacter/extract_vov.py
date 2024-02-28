import re
sequence="SIKANDAR BANGLORE"
pattern="[AEIOU]"
vov=re.findall(pattern,sequence)

# for ele in vov:
#     index=re.search(ele,sequence).start()
#     print(ele,index)

for ele in re.finditer('[AEIOU]', sequence):
    print(ele.start(), ele.group())