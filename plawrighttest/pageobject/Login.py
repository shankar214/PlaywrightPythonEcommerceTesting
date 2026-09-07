


from plawrighttest.pageobject.dashboardpage import DashBoardPage


class LoginPage:
    def __init__(self,page):
        self.page=page


    def navigatelink(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    def login(self,useremail,userpassword):

        self.page.locator("#userEmail").fill(useremail)
        self.page.locator("#userPassword").fill(userpassword)
        self.page.locator("#login").click()
        dashboardpage=DashBoardPage(self.page)
        return dashboardpage