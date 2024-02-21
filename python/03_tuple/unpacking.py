myTuple=("Apple", "banana", "mango")
(red, green, yell)=myTuple
print(red)
print(green)
print(yell)



# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Example
# Assign the rest of the values as a list called "red":

number=(1,2,3,4,5,6,7,8,9)
(one, two, *remain)=number
print(one)
print(two)
print(remain)


(one, *two, remain)=number
print(one)
print(two)
print(remain)



