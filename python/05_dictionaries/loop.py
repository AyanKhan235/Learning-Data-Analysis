User={
    "name":"AYANKHAN",
    "age":21,
    "course":"B-tech",
    "college":"techno",
    "back":False,
    "cgpa":75,
    # "age":33 # it overwright value
    "name":"AYANKHAN",
    "color":["red", "yellow", "blue"]

}


# for x in User:
#     # print(x)
#     # print(User[x])

for x in User.values():
    print(x)
for x in User.keys():
    print(x)
for x, y in User.items():
  print(x, y)
