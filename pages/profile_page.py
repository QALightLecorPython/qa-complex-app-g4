"""Profile PageObject"""

from selenium.webdriver.common.by import By

from constants.profile_page import ProfilePageConstants
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class ProfilePage(BasePage):
    """Profile PageObject"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ProfilePageConstants()
        self.header = Header(driver)

    @log_wrapper
    def follow_user_and_verify(self, owner_username, username):
        """Follow user and verify the result"""
        self.click(self.constants.FOLLOW_BUTTON_XPATH)
        self.wait_until_displayed(
            self.constants.FOLLOWERS_TAB_XPATH.format(
                username=owner_username.lower()
            )
        ).click()
        followers = self.driver.find_elements(
            by=By.XPATH, value=self.constants.FOLLOWERS_LIST_XPATH
        )
        follower_nicks = [follower.text.strip() for follower in followers]
        assert username.lower() in follower_nicks

    @log_wrapper
    def verify_followings(self, owner_username, username):
        """Verify following tab data"""
        self.wait_until_displayed(
            self.constants.FOLLOWING_TAB_XPATH.format(
                username=owner_username.lower()
            )
        ).click()
        followings = self.driver.find_elements(
            by=By.XPATH, value=self.constants.FOLLOWERS_LIST_XPATH
        )
        following_nicks = [follower.text.strip() for follower in followings]
        assert username.lower() in following_nicks

    @log_wrapper
    def navigate_to_the_post(self, title):
        """Navigate to post from list using title"""
        # pylint: disable=import-outside-toplevel
        posts = self.driver.find_elements(
            by=By.XPATH, value=self.constants.POSTS_LIST_XPATH
        )
        for post in posts:
            if post.text == title:
                post.click()
        from pages.post_page import PostPage

        return PostPage(self.driver)

    @log_wrapper
    def verify_deleted_message_text(self) -> None:
        """Verify success post creation message"""
        element = self.wait_until_displayed(
            self.constants.POST_DELETED_MESSAGE_XPATH
        )
        assert element.text == self.constants.POST_DELETED_MESSAGE_TEXT

    @log_wrapper
    def verify_posts_count(self, expected_count: int):
        """Verify number of posts for the user"""
        # Verify tab text
        posts_tab = self.wait_until_displayed(self.constants.POSTS_TAB_XPATH)
        tab_posts_count = int(posts_tab.text.split()[1])
        assert (
                tab_posts_count == expected_count
        ), f"Actual: {tab_posts_count}, Expected: {expected_count}"

        # Verify actual posts list
        posts = self.driver.find_elements(
            by=By.XPATH, value=self.constants.POSTS_LIST_XPATH
        )
        assert (
                len(posts) == expected_count
        ), f"Actual: {len(posts)}, Expected: {expected_count}"

    @log_wrapper
    def verify_post_not_present(self, title: str):
        """Verify that post is not on the page"""
        posts = self.driver.find_elements(
            by=By.XPATH, value=self.constants.POSTS_LIST_XPATH
        )
        for post in posts:
            if post.text == title:
                raise AssertionError(f"Post '{title}' is in the list")
