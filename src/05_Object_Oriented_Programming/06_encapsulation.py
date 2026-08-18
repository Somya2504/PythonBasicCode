class BankAccount:
    Bank_Name = "HDFC"

    # In Python, private variable is __X
    def __init__(self, __acc_no, __balance, __pin):
        self.__acc_no = __acc_no
        self.__balance = __balance
        self.__pin = __pin

    def display_account_details(self):
        print("*" * 50)
        print(f"Bank Name: {self.Bank_Name}")
        print(f"Account No.: {self.__acc_no}")
        print(f"Balance: {self.__balance}")
        print("*" * 50)

    def deposit(self):
        self.amount = float(input("Please enter the amount to be deposited: "))
        if self.amount > 0:
            self.__balance += self.amount
            self.display_account_details()
        else:
            print("Please enter a valid amount.")

    def withdraw(self):
        self.amount = float(input("Please enter the amount to be withdrawn: "))
        if self.amount > 0 and self.amount <= self.__balance:
            self.__balance -= self.amount
            self.display_account_details()
        else:
            print("Insufficient Balance.")

    def check_balance(self):
        return self.__balance

    def change_pin(self):
        self.old_pin = int(input(f"Provide your Old PIN: "))

        if self.old_pin == self.__pin:
            self.new_pin = int(input(f"Provide your New PIN: "))
            if self.new_pin == self.old_pin:
                print("This PIN has already been provided.")
            else:
                self.__pin = self.new_pin
        else:
            print("Existing PIN is not provided.")

account = BankAccount(703685, 385257, 7025)

account.display_account_details()
account.deposit()
account.withdraw()
print(f"Current Balance: {account.check_balance()}")
account.change_pin()
#print(account.__balance)
print(account.__dict__)

