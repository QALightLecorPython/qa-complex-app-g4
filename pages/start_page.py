"""Start PageObject"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.hello_user_page import HelloUserPage
from pages.utils import User, log_wrapper, wait_until_ok


class StartPage(BasePage):
    """Start PageObject"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    @log_wrapper
    def sign_in(self, user: User) -> HelloUserPage:
        """Sign in using provided values"""
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_XPATH, value=user.password)
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)
        return HelloUserPage(self.driver)

    @log_wrapper
    def verify_sign_in_error(self) -> None:
        """Verify error on invalid sign in"""
        error_message = self.wait_until_displayed(xpath=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        assert error_message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT, "Text is not valid"

    @log_wrapper
    def sign_up_and_verify(self, user: User) -> HelloUserPage:
        """Sign up the user using provided values and verify the result"""
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        self.click_sign_up_and_verify()
        return HelloUserPage(self.driver)

    @log_wrapper
    def sign_up(self, user: User):
        """Sign up the user using provided values"""
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    @wait_until_ok(timeout=10, period=1)
    @log_wrapper
    def click_sign_up_and_verify(self) -> None:
        """Click sign up and verify that button doesn't exists anymore"""
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        assert not self.is_element_exists(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    @wait_until_ok(timeout=5)
    @log_wrapper
    def verify_sign_up_validation_error(self, text):
        """Verify validation error for any sign up field"""
        validation_errors = self.driver.find_elements(by=By.XPATH, value=self.constants.SIGN_UP_FIELD_VALIDATION_MESSAGE)
        visible_errors = [element for element in validation_errors if element.is_displayed()]
        assert len(visible_errors) == 1, f"Actual: {len(visible_errors)}"
        assert visible_errors[0].text == text, f"Actual: {visible_errors[0].text}"
