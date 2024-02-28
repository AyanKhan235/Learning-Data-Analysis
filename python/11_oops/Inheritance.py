class Person:
    def __init__(self, name, password):
        self.name=name
        self.password=password
    def printName(self):
        print('user name is', self.name)
# x=Person('john',123)
# x.printName()
# Create a class named Student, which will inherit the properties and methods from the Person class:

# class Student(Person):
#     def __init__(self, name, password):
#         # Person.__init__(self,name, password)
#         super().__init__(name, password)
#         # Add a property called graduationyear to the Student class:
#         self.graduationyear=2025


# s=Student('ayan', 123)
# s.printName()
# print(s.graduationyear)

class Student(Person):
  def __init__(self, name, password, year):
    super().__init__(name, password)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.name, self.password, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.printName()
print(x.graduationyear)
x.welcome()
