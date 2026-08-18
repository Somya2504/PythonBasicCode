class Employee:

    def __init__(self, employee_id, employee_name, Salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.Salary = Salary
        print("Employee constructor")

    def display_details(self):
        print(f"Employee ID     : {self.employee_id}")
        print(f"Employee Name   : {self.employee_name}")
        print(f"Salary          : {self.Salary}")

# Inheritance
class Manager(Employee):

    def __init__(self, employee_id, employee_name, Salary, team_size):
        super().__init__(employee_id, employee_name, Salary)
        self.team_size = team_size
        print("Manager constructor")

    def display_details(self):
        print("*" * 50)
        #Employee.display_details(self)
        super().display_details()     #super() is used to Call the parent class's display_details() method using the current object
        print(f"Team Size       : {self.team_size}")

    def approve_leave(self):
        print(f"Approving the leave request for {self.employee_id} - {self.employee_name}")

manager = Manager(420, "Dharmendhar Pradhan", 150000, 8)

manager.display_details()
manager.approve_leave()

print("*" * 50)

# Multilevel Inheritance
class SeniorManager(Manager):

    def __init__(self, employee_id, employee_name, Salary, team_size, department_name):
        super().__init__(employee_id, employee_name, Salary,team_size)
        self.department_name = department_name
        print("Senior Manager constructor")
        
    def display_details(self):
        super().display_details()
        print(f"Department Name : {self.department_name}")
        print("*" * 50)

    def confirm_leave_request(self):
        print(f"Leave request for '{self.employee_id} - {self.employee_name}' has been approved.")

    def conduct_review(self):
        print(f"Conducting review for {self.employee_id} - {self.employee_name}")

senior_manager = SeniorManager(876, "Amit Saha", 150000, 8, department_name= "Sales")

senior_manager.display_details()
senior_manager.confirm_leave_request()
senior_manager.conduct_review()

print(SeniorManager.mro())  #Python's MRO — Method Resolution Order tells Python the order in which it searches for a method.

