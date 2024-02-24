# $ end with 
import re
text="the rain in Spain"
x=re.findall("Spain$", text)
print(x)