# Multiple Inheritance

# Parent_1
class Employee:

    def work(self):
        print("Employee is performing business operations.")
        super().work()      #super() means "continue to the next class according to MRO."

# Parent_2
class TechnicalLead:
    def work(self):
        print("Technical Lead is designing the automation framework.")
        #super().work()

# Child
class TechManager(Employee, TechnicalLead):
    def work(self):
        print("Tech Manager is monitoring the operations.")
        super().work()

tech_manager = TechManager()
tech_manager.work()

print(TechManager.mro())

# isinstance() — Is this object an instance of this class?
print(isinstance(tech_manager, Employee))       # True
print(isinstance(tech_manager, TechnicalLead))  # True
print(isinstance(tech_manager, TechManager))    # True
print(isinstance(tech_manager, str))            # False

print("*" * 50)

# issubclass() — Is this class a child of another class?
print(issubclass(TechManager, Employee))      # True
print(issubclass(TechManager, TechnicalLead))   # True
print(issubclass(TechnicalLead, Employee))      # False