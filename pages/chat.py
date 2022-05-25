from typing import List

from selenium.webdriver import Keys

from constants.chat import ChatConstants
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_wrapper


class Chat(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ChatConstants()

    @log_wrapper
    def send_message(self, message: str) -> None:
        """Send message to the chat"""
        self.fill_field(xpath=self.constants.CHAT_INPUT_FIELD_XPATH, value=message + Keys.ENTER)

    @wait_until_ok()
    @log_wrapper
    def verify_messages(self, expected_messages: List[str]):
        """Verify actual messages match to the expected"""
        elements = self.wait_until_elements_displayed(self.constants.CHAT_MESSAGES_XPATH)
        actual_messages = [element.text for element in elements]
        assert actual_messages == expected_messages, f"Actual: {actual_messages}, Expected: {expected_messages}"
