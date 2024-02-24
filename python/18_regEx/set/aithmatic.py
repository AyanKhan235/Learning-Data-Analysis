import re

txt = "8 times before 11:45 AM"

#Check if the string has any + characters:

add= re.findall("[+]", txt)
mul= re.findall("[*]", txt)
div= re.findall("[/]", txt)
mod= re.findall("[%]", txt)



print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")