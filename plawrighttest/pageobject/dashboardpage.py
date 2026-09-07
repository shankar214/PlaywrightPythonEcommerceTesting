from plawrighttest.pageobject.orderhistorypage import OrderHistoryPage


class DashBoardPage:
    def __init__(self,page):
        self.page=page

    def Selectordernavilink(self):
        self.page.locator('//button[@routerlink="/dashboard/myorders"]').click()
        orderhistorypage=OrderHistoryPage(self.page)
        return orderhistorypage
