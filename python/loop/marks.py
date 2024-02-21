marks=[99,44,37,0]
for x in marks:
    if x< 36:
        print(x, "fail")
        result=0;
     
    else:
        print(x, "pass")
        result=1
 
if result==0:
    print("You are failed")
else: 
    print("You are passed")