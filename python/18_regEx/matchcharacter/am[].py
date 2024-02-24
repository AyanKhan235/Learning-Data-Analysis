import re
text="The rain is Spain"
x=re.findall("[A-Z]", text)
print(x)
x=re.findall("[a-z]", text)

print(x)