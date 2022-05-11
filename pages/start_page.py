from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def sign_in(self, username="", password=""):
        """Sign in using provided values"""
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_XPATH, value=password)
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)

    def verify_sign_in_error(self):
        """Verify error on invalid sign in"""
        error_message = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        assert error_message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT, "Text is not valid"

    def sign_up(self, user):
        """Sign up the user using provided values"""
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        sleep(1)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    def verify_success_sign_up(self, username):
        """Verify hello message for a new user"""
        hello_message = self.driver.find_element(by=By.XPATH, value=self.constants.SUCCESS_MESSAGE_XPATH)
        assert username.lower() in hello_message.text
        assert hello_message.text == self.constants.SUCCESS_MESSAGE_TEXT.format(username=username.lower())
        assert self.driver.find_element(by=By.XPATH, value=self.constants.SUCCESS_MESSAGE_USERNAME_XPATH).text == username.lower()

    # FixMe: Move to ProfilePage object once created
    def logout(self):
        self.click(self.constants.SIGN_OUT_BUTTON_XPATH)
