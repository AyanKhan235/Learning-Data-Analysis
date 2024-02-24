# try:
#     print(x)
# except:
#     print("An exeption ocuur")

# print(x)

# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

# Example
# Print one message if the try block raises a NameError and another for other errors:
# try:
#     print(x)
# except NameError:
#     print("Variable is not defined")
# except:
#     print("Something is wrong")


#  try block does not generate any erro
# try:
#     print('helo')
# except:
#     print('Something is Wrong')
# else:
#     print('Nothing is wrong')




# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

# Example
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")



# try:
#     f = open('demofile.txt')
#     try:
#         f.write("lorem")
#     except:
#         print('Something is wrong when file open')
#     finally:
#         f.close()
# except:
#     print("Something is wrong when file open")


# x=-1
# if x < 0:
#     raise Exception("Sorry no number is below zero")



x='hello'
if not type(x) is int:
    raise TypeError("only integers are allow")