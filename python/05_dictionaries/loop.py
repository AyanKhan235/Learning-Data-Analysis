# User={
#     "name":"AYANKHAN",
#     "age":21,
#     "course":"B-tech",
#     "college":"techno",
#     "back":False,
#     "cgpa":75,
#     # "age":33 # it overwright value
#     "name":"AYANKHAN",
#     "color":["red", "yellow", "blue"]

# }


# for x in User:
#     # print(x)
#     # print(User[x])

# for x in User.values():
#     print(x)
# for x in User.keys():
#     print(x)
# for x, y in User.items():
#   print(x, y)

list1=[14,8,10,18,18,3,10,17,6,11,14,19,14,7,8,16,18,10,6,0]
freq={}
print(freq)
for ele in list1:
    x=freq.get(ele,0)
    freq[ele]=x+1
       
print(freq)