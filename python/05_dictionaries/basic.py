# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict={
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

print(thisdict)
print(thisdict["name"])
print(len(thisdict))
print(thisdict["color"])
print(type(thisdict))



new = dict(name = "John", age = 36, country = "Norway")
print(new)