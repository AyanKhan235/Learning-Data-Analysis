import json
# x='{"name":"Ayan", "age":21,"city":"Udaipur"}'
# # Convert from JSON to Python:
# y=json.loads(x)
# print(y["age"])


x={
    "name":"AYAN",
    "age":21,
    "city":"Udaipur"
}

# convert python to json
y=json.dumps(x)
print(y)

# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None


# Convert Python objects into JSON strings, and print the values:

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))





x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x)) #not easy to read 
print(json.dumps(x,indent=10) )  # easy to read indent number greter easy to understand

# u can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

# Example
# Use the separators parameter to change the default separator:

print(json.dumps(x, indent=4, separators=(". ", " = ")))


