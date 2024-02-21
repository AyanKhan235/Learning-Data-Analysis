import math 
def quardEquation(a,b,c):
    x1=(-b + math.sqrt(b**2 - 4*a*c))/2*a
    x2=(-b - math.sqrt(b**2 - 4*a*c))/2*a
    # b value should be greater the use this 
    return x1,x2

if __name__ == "__main__":
    print("program to calculate Quardratic Equation")
    a=int(input("Enter the value of a :"))
    b=int(input("Enter the value of b :"))
    c=int(input("Enter the value of c :"))

    x1,x2=quardEquation(a,b,c)
    print(x1,x2)