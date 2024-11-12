# Add class Base to components/base.py
# Add def click method that uses explicit wait (element_to_be_clickable)
# Add def find_element that uses  explicit wait (visibility_of_element_located)
# Add more as needed and use them in your code

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    def find_element(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element
