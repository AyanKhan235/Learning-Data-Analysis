import re
text="The rain in spain"
# start with s untill the finish
# Zero or more occurrences
x=re.findall("s.*",text)
y=re.findall("T.*", text)
print(y)
print(x)