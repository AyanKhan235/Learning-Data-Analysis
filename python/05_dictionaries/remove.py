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


User.pop("back")
# print(User)
User.popitem()
print(User)



del User["age"]
print(User)



User.clear()
print(User)
del User
print(User)