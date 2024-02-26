class Student:
    def __init__(self,regno,name,marks=1):
        self.regno=regno
        self.name=name
        self.marks=marks 
    def __str__(self):
        print(f"object id is {id(self)} created")
        return str(self.regno)+ " " +self.name+ " " +str(self.marks)
    def __del__(self):
        print(f"Object {id(self)} destroyed")
s1=Student(32,"AYANPATHAN")
# s2.Student(22)

print(s1)
s2=Student(33,"pathan")
print(s2)
# print("Reg No: ",s1.regno)
# print("Reg No: ",s1.name)
# print("Reg No: ",s1.sem)


# class Student:
#     pass
# s1=Student()
# s1.name="ayan"
# print(s1.name)
# s2=Student
# print(s2.name)
