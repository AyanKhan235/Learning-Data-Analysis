
def checkVovel(str):
    flag=True
    for x in str:
        if x in "aeiou":
            flag=True
            
        else:
            flag=False
            break;

    if flag:
        print("Happy")
    else:
        print("False")

def fullString(string):
    for x in range(len(string)):
        checkVovel(string.slice[x:x+3])


fullString("nameayankhan")
