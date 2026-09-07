import json
from pathlib import Path

from playwright.sync_api import Playwright
from playwright.sync_api import expect
from plawrighttest.pageobject.Login import LoginPage

from plawrighttest.utils.apiBase import Apiutil

import pytest

BASE_DIR = Path(__file__).resolve().parent
with open(BASE_DIR / 'data' / 'credentials.json') as f:
    test_data = json.load(f)
    user_credentials_list = test_data['usercredentials']


@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_e2e_web_api(playwright,browserinstance,user_credentials):
    page=browserinstance
    useremail=user_credentials["userEmail"]
    userpassword=user_credentials["userPassword"]

    #createorder
    api_utils=Apiutil()
    orderid=api_utils.createOrder(playwright,user_credentials)
    #json files->util->acces test
   


    #login page
    loginpage=LoginPage(page)
    loginpage.navigatelink()
    dashboardpage=loginpage.login(useremail,userpassword)
    
    #dashboard page
    orderhistorypage=dashboardpage.Selectordernavilink()
    verifytheorder=orderhistorypage.selectorder(orderid)
    verifytheorder.verfiytheorder()
    print("code completed")
    #recording trace to each step by seeing the failure in the test case
    #genearate html report for the test case --html=report.html
    #prallel testing --workers pipinstall->xdist
    #pytest -n 3
    #pytest --browsername chrome m smoke -n 3 --tracing on --html=report.htmlpy 
    
