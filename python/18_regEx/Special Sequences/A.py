import re
text="The rain is spain"
#Check if the string starts with "The":
x=re.findall("\AThe", text)
print(x)