import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^heloo", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
