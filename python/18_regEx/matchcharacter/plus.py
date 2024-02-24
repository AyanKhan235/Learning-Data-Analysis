import re
text="The rain in Spain"
# One or more occurrences
x=re.findall("T.+", text)
print(x)