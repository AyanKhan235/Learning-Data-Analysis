price=49
text="The Price is {} dollar"
text2="The Price is {:.2f} dollar"
print(text.format(price))
print(text2.format(price))

newtext="I want {} pieces of item number {} for {:.2f} dollars."
quantity=4
itemNo=546
price=48
print(newtext.format(quantity,itemNo,price))


quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))