

import playwright
import pytest




@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param
@pytest.fixture(scope="session")
def browserinstance(playwright):
    browser = playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    yield page
    page.close()
