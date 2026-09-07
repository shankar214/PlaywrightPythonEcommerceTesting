from plawrighttest.pageobject.orderdetailspage import ordersdetails


class OrderHistoryPage:
    def __init__(self,page):
        self.page=page
    def selectorder(self,orderid):
          
         row=self.page.locator("tr").filter(has_text=orderid)
         row.get_by_role('button',name="View").click()
         veriftheorder=ordersdetails(self.page)
         return veriftheorder
   