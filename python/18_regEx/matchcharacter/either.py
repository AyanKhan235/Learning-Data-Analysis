import re
text= "The rain in spain"
x= re.findall("The|coca", text)
print(x)