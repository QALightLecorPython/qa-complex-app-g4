from constants.hello_user_page import HelloUserPageConstants
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class HelloUserPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HelloUserPageConstants()
        self.header = Header(driver)

    @log_wrapper
    def verify_success_sign_up(self, username):
        """Verify hello message for a new user"""
        hello_message = self.wait_until_displayed(xpath=self.constants.SUCCESS_MESSAGE_XPATH)
        assert username.lower() in hello_message.text
        assert hello_message.text == self.constants.SUCCESS_MESSAGE_TEXT.format(username=username.lower())
        assert self.wait_until_displayed(xpath=self.constants.SUCCESS_MESSAGE_USERNAME_XPATH).text == username.lower()
