total=0
def add(a, b):
    #  if we do not use global so total will be new varibale and cannot access value it will remain same out of funvtion
    #  global variale hi use hoga otherwise locat create hoga
    global total
    total=a+b
    print("inside total", total)
add(4,9)
print(total)