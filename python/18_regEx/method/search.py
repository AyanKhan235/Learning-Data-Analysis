import re
text="The rain in spain"
# x=re.search("sp", text) # give index
x=re.search("\s", text) # give index // double character not allow


# y=re.search("noone", text)
print("the first character start index with ",x.start())
# print("the first character start index with ",x.end())
