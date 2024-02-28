import re
phoneNo=["7014055235", "123456982", "5480552277", "9024292907"]
pattern="[7-9]\d{9}$"
for phone in phoneNo:
    if re.match(pattern, phone)!=None:
        print("Phone no is valid ", phone)
    else:
        print("Not valid ", phone)
