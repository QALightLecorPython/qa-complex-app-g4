from time import sleep

from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    @log_wrapper
    def sign_in(self, user):
        """Sign in using provided values"""
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_XPATH, value=user.password)
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)

    @log_wrapper
    def verify_sign_in_error(self):
        """Verify error on invalid sign in"""
        error_message = self.wait_until_displayed(xpath=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        assert error_message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT, "Text is not valid"

    @log_wrapper
    def sign_up(self, user):
        """Sign up the user using provided values"""
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        sleep(1)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    @log_wrapper
    def verify_success_sign_up(self, username):
        """Verify hello message for a new user"""
        hello_message = self.wait_until_displayed(xpath=self.constants.SUCCESS_MESSAGE_XPATH)
        assert username.lower() in hello_message.text
        assert hello_message.text == self.constants.SUCCESS_MESSAGE_TEXT.format(username=username.lower())
        assert self.wait_until_displayed(xpath=self.constants.SUCCESS_MESSAGE_USERNAME_XPATH).text == username.lower()

    # FixMe: Move to ProfilePage object once created
    @log_wrapper
    def logout(self):
        """Sign out from user profile"""
        self.click(self.constants.SIGN_OUT_BUTTON_XPATH)
