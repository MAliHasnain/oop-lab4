class Employee:
    def __init__(self,employee_id,employee_name,designation):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.designation = designation
    def print(self):
        print(f"The name of employee is : {self.employee_name} ")
        print(f"The employee's id is {self.employee_id} ")
        print(f"The designation of the employee is {self.designation} ")
class Manager(Employee):
    def __init__(self,employee_id,employee_name,designatiom,branch_name):
        super().__init__(employee_id,employee_name,designatiom)
        self.branch_name = branch_name
    def print(self):
        super().print()
        print(f"He is the manager of {self.branch_name} ......")
class Team_lead(Employee):
    def __init__(self,employee_id,employee_name,designation,no_of_members):
        super().__init__(employee_id,employee_name, designation)
        self.no_of_members = no_of_members
    def print(self):
        super().print()
        print(f"Number of members in his team are {self.no_of_members} ......")
class Clerk(Employee):
    def __init__(self,employee_id,employee_name,designation,salary):
        super().__init__(employee_id,employee_name, designation)
        self.salary = salary
    def print(self):
        super().print()
        print(f"The salary of this empolyee is {self.salary} ......")
m1 = Manager(1,"Hasnain","Manager","Clifton branch")
m1.print()
t1 = Team_lead(2,"Akhtar","Team lead",8)
t1.print()
c1 = Clerk(3,"Danish","Clerk",25000)
c1.print()


















