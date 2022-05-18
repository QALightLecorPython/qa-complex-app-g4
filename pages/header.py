from constants.header import HeaderConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConstants()

    @log_wrapper
    def logout(self):
        """Sign out from user profile"""
        self.click(self.constants.SIGN_OUT_BUTTON_XPATH)
        from pages.start_page import StartPage
        return StartPage(self.driver)

    @log_wrapper
    def navigate_to_create_post(self):
        """Navigate to create post page"""
        self.click(self.constants.CREATE_POST_BUTTON_XPATH)
        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)
