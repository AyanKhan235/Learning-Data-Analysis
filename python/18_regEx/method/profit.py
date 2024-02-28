import re
sequencee=" the purchase price is 2000 and selling price is 2345"
patter='\d+'
number=re.findall(patter,sequencee)
# number=re.search(patter,sequencee) // it give basically first number

print(number)
# number=list(number)
# profit=int(number[1])-int(number[0])
# print(profit)
# num1=int(number[1])
# num2=int(number[0])
