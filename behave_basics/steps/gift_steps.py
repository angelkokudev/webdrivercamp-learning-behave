from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from behave_basics.components.base import Base


@step("Navigate to {url}")
def step_impl(context, url):
    context.browser.get(url)
    context.base = Base(context.browser)


@step("Search for {search_item}")
def step_impl(context, search_item):
    search_locator = (By.XPATH, '//*[@id="search"]')
    search_field = context.base.find_element(search_locator)
    search_field.send_keys(search_item)
    search_field.send_keys(Keys.RETURN)


@step("Verify header of the page contains {search_item}")
def step_impl(context, search_item):
    header_locator = (By.XPATH, f"//h1[contains(.,'{search_item}')] | f//span[contains(., '{search_item}')]")
    page_header = WebDriverWait(context.browser, 10).until(presence_of_element_located(header_locator))
    assert search_item.lower() in page_header.text.lower(), f"Expected {search_item} to be {page_header.text}"








