"""Post PageObject"""

from constants.post_page import PostPageConstants
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


# pylint: disable=import-outside-toplevel
class PostPage(BasePage):
    """Post PageObject"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = PostPageConstants()
        self.header = Header(driver)

    @log_wrapper
    def navigate_to_user_profile(self, username):
        """Navigate to user profile page"""
        self.click(
            self.constants.LINK_TO_USER_PROFILE_XPATH.format(
                username=username.lower()
            )
        )
        from pages.profile_page import ProfilePage

        return ProfilePage(self.driver)

    @log_wrapper
    def edit_post(self):
        """Navigate to post edit page"""
        self.click(self.constants.EDIT_POST_BUTTON_XPATH)
        from pages.create_post_page import UpsertPostPage

        return UpsertPostPage(self.driver)

    @log_wrapper
    def verify_post_data(self, title: str, content: str):
        """Verify post's data"""
        actual_title = self.wait_until_displayed(
            self.constants.TITLE_TEXT_XPATH
        )
        assert (
                actual_title.text == title
        ), f"Actual: {actual_title}, Expected: {title}"
        actual_content = self.wait_until_displayed(
            self.constants.CONTENT_TEXT_XPATH
        )
        assert (
                actual_content.text == content
        ), f"Actual: {actual_content}, Expected: {content}"

    @log_wrapper
    def delete_post(self):
        """Delete post"""
        self.click(self.constants.DELETE_POST_BUTTON_XPATH)
        from pages.profile_page import ProfilePage

        return ProfilePage(self.driver)
