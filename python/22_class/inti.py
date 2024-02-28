class Student:
    def __init__(self,regno,name,marks=1):
        self.regno=regno
        self.name=name
        self.marks=marks 
    def __str__(self):
        print(f"object id is {id(self)} created")
        return str(self.regno)+ " " +self.name+ " " +str(self.marks)
    # def  __gt__(self,s2):
    #     return self.marks > s2.marks
    def __It__(self,s2):
        print("less than")
        return self.marks > s2.marks
    # def __del__(self):
    #     print(f"Object {id(self)} destroyed")
s1=Student(32,"AYANPATHAN")
# s2.Student(22)

print(s1)
s2=Student(33,"pathan")
print(s2)
if s1 < s2:
    print("AYANKHAN is largest")
else:
    print("pathan")

