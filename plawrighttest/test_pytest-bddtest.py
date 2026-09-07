



import pytest
from pytest_bdd import given, scenarios, then, when, parsers

from plawrighttest.pageobject.Login import LoginPage
from plawrighttest.utils.apiBase import Apiutil


scenarios('features/ordertransaction.feature')
@pytest.fixture
def shared_data():
    return{}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_iteam_order(playwright, username, password,shared_data):
    user_credentials={}
    user_credentials['userEmail']=username
    user_credentials['userPassword']=password
    api_utils=Apiutil()
    orderid=api_utils.createOrder(playwright, user_credentials)
    shared_data['orderid']=orderid
@given('the user is on landing page')
def user_on_landing_page(browserinstance,shared_data):
    loginpage=LoginPage(browserinstance)
    loginpage.navigatelink()
    shared_data['loginpage']=loginpage

@when(parsers.parse('I Login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    loginpage=shared_data['loginpage']
    dashboardpage=loginpage.login(username, password)
    shared_data['dashboardpage']=dashboardpage
@when('navigate to the orders page')
def navigate_to_orders_page(shared_data):
    dashboardpage=shared_data['dashboardpage']
    orderhistorypage=dashboardpage.Selectordernavilink()
    shared_data['orderhistorypage']=orderhistorypage
@when('select the orderId')
def select_order_id(shared_data):
    orderhistorypage=shared_data['orderhistorypage']
    orderid=shared_data['orderid']
    verifytheorder=orderhistorypage.selectorder(orderid)
    shared_data['verifytheorder']=verifytheorder




@then('order message is succesfully displayed')
def order_message_successfully_displayed(shared_data):
    verifytheorder=shared_data['verifytheorder']
    verifytheorder.verfiytheorder()