import re
sequence="sikandar banglore"
pattern="an"
# res=re.match(pattern,sequence)
# res=re.search(pattern,sequence)
# res=re.findall(pattern,sequence) # return  list
res=re.finditer(pattern,sequence)

for ele in res:
    print(sequence[ele.start():])



# if res!=None:
#     print("matching string",res.group())
#     print("begin Index",res.start())
#     print("End Index",res.end())
#     print("span",res.span())

# if res == None:
#     print("Does not begin with ", pattern)
# else:
#     print("begin with ", pattern)


