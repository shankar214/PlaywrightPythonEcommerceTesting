from playwright.sync_api import Playwright
orderpayload={"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}


class Apiutil:


    def gettoken(self,plawright:Playwright,user_credentials):
        user_email=user_credentials["userEmail"]
        user_password=user_credentials["userPassword"]
        api_request_context=plawright.request.new_context(base_url="https://rahulshettyacademy.com/",ignore_https_errors=True)
        response=api_request_context.post("api/ecom/auth/login",data={"userEmail": user_email, "userPassword":user_password})
        response.ok
        print(response.json())
        responsebody=response.json()
        return responsebody["token"]


    
    def createOrder(self,playwright:Playwright,user_credentials):
       print("Inside createOrder")
       token=self.gettoken(playwright,user_credentials)
       api_request_context= playwright.request.new_context(base_url="https://rahulshettyacademy.com/",ignore_https_errors=True)
       response = api_request_context.post(
    "api/ecom/order/create-order",
    data=orderpayload,
    headers={
        "Authorization": token,
        "Content-Type": "application/json"
    }

)
       responsebody=response.json()
       orderids=responsebody["orders"][0]
       return orderids
       print("Order Response:")
       print(response)