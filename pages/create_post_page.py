from constants.create_post_page import CreatePostPageConstants
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class CreatePostPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostPageConstants()
        self.header = Header(driver)

    @log_wrapper
    def create_post(self, title, content):
        """Creates post as a user using provided values"""
        self.fill_field(self.constants.TITLE_FIELD_XPATH, title)
        self.fill_field(self.constants.CONTENT_FIELD_XPATH, content)
        self.click(self.constants.SAVE_POST_BUTTON_XPATH)

    @log_wrapper
    def verify_message_text(self):
        """Verify success post creation message"""
        element = self.wait_until_displayed(self.constants.SUCCESS_MESSAGE_XPATH)
        assert element.text == self.constants.SUCCESS_MESSAGE_TEXT
