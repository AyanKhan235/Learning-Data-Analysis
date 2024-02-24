import re
text="hello planet"
x=re.findall("he.{2}o", text)
print(x)