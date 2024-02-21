number=int(input("Enter a number"))

# i=1
# while i <= number:
#     print(i)
#     i=i+1

i=0
while number!=0:
    number//=10
    i=i+1
print(i)
