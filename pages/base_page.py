"""Base PageObject"""
import random
import string
from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.utils import time_out_wrapper


class BasePage:
    """Base PageObject"""

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    @staticmethod
    def random_num() -> str:
        """Generate random number"""
        return str(random.randint(111111, 999999))

    @staticmethod
    def random_str(length=5):
        """Generate random string"""
        return "".join(random.choice(string.ascii_letters) for _ in range(length))

    @time_out_wrapper
    def wait_until_clickable(self, xpath: str) -> WebElement:
        """Waits until element is clickable"""
        return self.waiter.until(method=expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

    @time_out_wrapper
    def wait_until_displayed(self, xpath: str) -> WebElement:
        """Waits until element is displayed"""
        return self.waiter.until(method=expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    @time_out_wrapper
    def wait_until_elements_displayed(self, xpath: str) -> List[WebElement]:
        """Wait until elements are displayed"""
        return self.waiter.until(method=expected_conditions.visibility_of_all_elements_located((By.XPATH, xpath)))

    def is_element_exists(self, xpath: str) -> bool:
        """Check if element exists"""
        try:
            self.driver.find_element(by=By.XPATH, value=xpath)
            return True
        except (TimeoutError, NoSuchElementException):
            return False

    def fill_field(self, xpath: str, value: str) -> None:
        """Send data into the field"""
        field = self.wait_until_clickable(xpath)
        field.clear()
        field.send_keys(value)

    def click(self, xpath: str) -> None:
        """Find and click the element"""
        self.wait_until_clickable(xpath).click()
