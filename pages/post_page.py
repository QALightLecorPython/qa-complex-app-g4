from constants.post_page import PostPageConstants
from pages.base_page import BasePage
from pages.profile_page import ProfilePage
from pages.utils import log_wrapper


class PostPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = PostPageConstants()

    @log_wrapper
    def navigate_to_user_profile(self, username):
        """Navigate to user profile page"""
        self.click(self.constants.LINK_TO_USER_PROFILE_XPATH.format(username=username.lower()))
        return ProfilePage(self.driver)
