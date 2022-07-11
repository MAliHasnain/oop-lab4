class Person:
    def __init__(self,name):
        self.name=name
    def print(self):
        print(self.name)
class Teacher(Person):
    def __init__(self,name,course_name):
        super().__init__(name)
        self.course_name=course_name
    def print(self):
        super().print()
        print(f"The course teach by {self.name} is {self.course_name} .")
class Student(Person):
    def __init__(self,name,dept,year):
        super().__init__(name)
        self.dept=dept
        self.year=year
    def print(self):
        super().print()
        print(f"The department of {self.name} is {self.dept} .\nThe batch year of {self.name} is {self.year} .")
t1=Teacher("Fauzia Yasir","Object Oriented Programming")
t1.print()
s1=Student("Muhammad Ali Hasnain","CIS",2021)
s1.print()
