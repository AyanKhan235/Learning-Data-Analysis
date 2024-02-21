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


User["home"]="nimbahera"
# print(User)



if "home" in  User:
    print("YEs hone is exist")
User.update({"home": "Udaipur"})
print(User)