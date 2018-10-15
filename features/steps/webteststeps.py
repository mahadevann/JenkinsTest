from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I navigate to the PyPi Home page')
def step_impl(context):
    context.browser.get("https://pypi.python.org/pypi")
    assert_equal(context.browser.title, "PyPI – the Python Package Index · PyPI")

@step('I search for "{search_term}"')
def step_impl(context, search_term):
    context.browser.find_element(By.ID, "search").send_keys(search_term)
    context.browser.find_element(By.CLASS_NAME, "search-form__button").click()

@step('I am taken to the PyPi Search Results page')
def step_impl(context):
    assert_equal(context.browser.title, "Index of Packages Matching 'behave' : Python Package Index")

@step('I see a search result "{search_result}"')
def step_impl(context, search_result):
    assert_true(context.browser.find_element(By.LINK_TEXT, search_result))
