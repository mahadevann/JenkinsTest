from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def before_all(context):
    webdriver.Remote(
            desired_capabilities=DesiredCapabilities.CHROME)
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()
