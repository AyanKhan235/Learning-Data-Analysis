class Student:  
    count=0
    def __int__(self, name=" ", marks=" ",regno=0):
        Student.count=Student.count+1
        self.regno=Student.count
        self.name=name
        self.marks=marks
    def __str__(self):
        return str(self.regno)+" "+self.name+" "+str(self.marks)
s1=Student("ayan", 80)
s2=Student("pathan", 50)
print(s1)