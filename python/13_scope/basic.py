# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()
# #  it cannot be access outside the function
# myfunc()


# x = 300
# #  its global

# def myfunc():
#   print(x)

# myfunc()

# print(x)




# Example
# The function will print the local x, and then the code will print the global x:

# x = 300

# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(x)



# If you use the global keyword, thxe variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()

print(x)