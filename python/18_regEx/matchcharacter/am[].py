import re
text="The rain 4646 is Spain 4764"
# x=re.findall("[A-Z]", text)
# print(x)
# y=re.findall("[a-z]", text)
# print(y)

# z=re.findall("[0-9]", text)
# print(z)
# none dgit
print(re.findall("[^0-9]", text))
# begin with num
print(re.findall("^[0-9]", text))
n=re.findall("\d", text)
m=re.findall("\D", text)

sequencee ="1234"
if re.search("\d",sequencee)!=None:
    print("Start with digit")
else:
    print("not start with digit")

New ="A1234"
if re.search("\d",New)!=None:
    print("Start with digit")
else:
    print("not start with digit")



