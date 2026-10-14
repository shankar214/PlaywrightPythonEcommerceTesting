import json
import json
from playwright.sync_api import Playwright
from playwright.sync_api import expect
from plawrighttest.pageobject.Login import LoginPage
from plawrighttest.utils.apiBase import Apiutil




def test_e2e_web_api(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    #createorder
    api_utils=Apiutil()
    orderid=api_utils.createOrder(playwright)
    #json files->util->acces test
    with open('data/credentials.json') as f:
        test_data=json.load(f)
        user_credentials_list=test_data[usercredentials]


    #login
    
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    #login
    page.locator("#userEmail").fill("shiva125@gmail.com")
    page.locator("#userPassword").fill("21it6051@R")
    page.locator("#login").click()
    page.wait_for_timeout(2000)
    page.locator('//button[@routerlink="/dashboard/myorders"]').click()
    print("succesfully excuted the code")
    row=page.locator("tr").filter(has_text=orderid)
    row.get_by_role('button',name="View").click()
    expect(page.locator('.tagline')).to_contain_text("Thank you for Shopping With Us")
    print("code completed")
    
    
