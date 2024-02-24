import re

#Split the string at every white-space character:

txt = "The rain in Spain"
# x = re.split("\s", txt)
# Split the string only at the first occurrence:
# x= re.split("\s", txt, 1)
# Replace every white-space character with the number 9:
x= re.split("\s","9", txt)
print(x)
