import re

#Split the string at every white-space character:

txt = "The rain in Spain"
# Replace every white-space character with the number 9:
# x= re.sub("\s","9", txt)
# x= re.sub("\s","9", txt, 2) # 2 times 
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())
