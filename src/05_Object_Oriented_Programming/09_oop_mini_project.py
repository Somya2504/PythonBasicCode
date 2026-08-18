class BasePage:
    def __init__(self, driver, page_url):
        self.driver   = driver
        self.page_url = page_url

    def open_page(self):
        print(f"Opening page: {self.page_url}")
        print(f"Using driver: {self.driver}")

    def close_page(self):
        print(f"Closing page: {self.page_url}")

class LoginPage(BasePage):

    def __init__(self, driver, page_url, username, __password):
        super().__init__(driver, page_url)
        self.username = username
        self.__password = __password

    def open_page(self):
        print("Opening Login page")
        super().open_page()

    def login(self):
        enter_username = input("Enter your username: ")
        enter_password = input("Enter your password: ")

        if enter_username != self.username:
            print("Incorrect Username")
            return

        if enter_password != self.__password:
            print("Incorrect Password")
            return

        print(f"Login Successful with username: {self.username}")
login_page = LoginPage("Chrome", "https://www.google.com", "Somyakanta", "Test@2504")

login_page.open_page()
login_page.login()
login_page.close_page()

print('*' * 50)

class DashboardPage(BasePage):

    def verify_dashboard(self):
        print("Dashboard loaded successfully.")

dashboard_page = DashboardPage("Chrome", "https://www.google.com")
dashboard_page.open_page()
dashboard_page.verify_dashboard()
dashboard_page.close_page()

print(isinstance(login_page, LoginPage))
print(isinstance(login_page, BasePage))

print(isinstance(dashboard_page, DashboardPage))
print(isinstance(dashboard_page, BasePage))


