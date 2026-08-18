class Employee:
    company_name = "CGI"

    def __init__(self,employee_id,employee_name, department, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Company Name  : {self.company_name}")
        print(f"Employee ID   : {self.employee_id}")
        print(f"Employee Name : {self.employee_name}")
        print(f"Department    : {self.department}")
        print(f"Salary        : {self.salary}")
        print("-" * 40)

employee_1 = Employee(501, "Alok Das", "Finance", 75000)
employee_2 = Employee(502, "Prem Chopda", "Law", 62500)
employee_3 = Employee(503, "Tarun Nair", "Marketing", 72500)

# Change the Class Variable
Employee.company_name = "NTT DATA"
employee_2.company_name = "Google"

# employee_1.display_details()
employees = [employee_1, employee_2, employee_3]

for employee in employees:
    employee.display_details()

print("-" * 40)

class irctc:

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

    def login(self):
        enter_userID = int(input("Enter User ID: "))

        if enter_userID != self.user_id:
            print("Incorrect User ID.")
            return
        enterPassword = input("Enter Password: ")

        if enterPassword == self.password:
            print("Login Successful")
        else:
            print("Incorrect Password")
railway = irctc(7035, "Sanya@122528")

railway.login()
