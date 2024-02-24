import re
text="The rain in Spain"
#Check if the string has other characters than a, r, or n:
x=re.findall("[^ran]", text)
print(x)