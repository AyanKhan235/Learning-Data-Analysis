import re
# text="The rain in spain"
# x=re.findall("[arnhd]",text) # all
# y=re.findall("[0123]", text)
# print(y)

# print(x)
text = "8 Times Before 11:45 AM"

#Check if the string has any digits:

# x = re.findall("[0-9]", txt)

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", text)

# Returns a match for any character alphabetically between a and z, lower case OR upper case
s=re.findall("[a-zA-Z]", text)
# print(x)
print(s)