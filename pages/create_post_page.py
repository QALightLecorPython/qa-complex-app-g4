"""Create Post PageObject"""
from constants.create_post_page import CreatePostPageConstants
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import Post, log_wrapper


class UpsertPostPage(BasePage):
    """Create Post PageObject"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostPageConstants()
        self.header = Header(driver)

    @log_wrapper
    def create_post(self, title: str, content: str) -> None:
        """Creates post as a user using provided values"""
        self.fill_field(self.constants.TITLE_FIELD_XPATH, title)
        self.fill_field(self.constants.CONTENT_FIELD_XPATH, content)
        self.click(self.constants.SAVE_POST_BUTTON_XPATH)

    @log_wrapper
    def create_post_with_share_option(self, post: Post) -> None:
        """Creates post as a user using provided values"""
        self.fill_field(self.constants.TITLE_FIELD_XPATH, post.title)
        self.fill_field(self.constants.CONTENT_FIELD_XPATH, post.text)
        self.click(self.constants.SHARE_OPTION_DROP_DOWN_XPATH)
        self.click(self.constants.SHARE_OPTION_MESSAGE_XPATH.format(option=post.share_option))
        self.click(self.constants.SAVE_POST_BUTTON_XPATH)

    @log_wrapper
    def update_post(self, title: str, content: str) -> None:
        """Updates post as a user using provided values"""
        self.fill_field(self.constants.TITLE_FIELD_XPATH, title)
        self.fill_field(self.constants.CONTENT_FIELD_XPATH, content)
        self.click(self.constants.UPDATE_POST_BUTTON_XPATH)

    @log_wrapper
    def verify_message_text(self) -> None:
        """Verify success post creation message"""
        element = self.wait_until_displayed(self.constants.SUCCESS_MESSAGE_XPATH)
        assert element.text == self.constants.SUCCESS_MESSAGE_TEXT

    @log_wrapper
    def verify_update_message_text(self) -> None:
        """Verify success post update message"""
        element = self.wait_until_displayed(self.constants.SUCCESS_MESSAGE_XPATH)
        assert element.text == self.constants.SUCCESS_UPDATE_MESSAGE_TEXT
