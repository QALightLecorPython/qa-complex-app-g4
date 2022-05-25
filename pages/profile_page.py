from selenium.webdriver.common.by import By

from constants.profile_page import ProfilePageConstants
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ProfilePageConstants()
        self.header = Header(driver)

    @log_wrapper
    def follow_user_and_verify(self, owner_username, username):
        """Follow user and verify the result"""
        self.click(self.constants.FOLLOW_BUTTON_XPATH)
        self.wait_until_displayed(self.constants.FOLLOWERS_TAB_XPATH.format(username=owner_username.lower())).click()
        followers = self.driver.find_elements(by=By.XPATH, value=self.constants.FOLLOWERS_LIST_XPATH)
        follower_nicks = [follower.text.strip() for follower in followers]
        assert username.lower() in follower_nicks

    @log_wrapper
    def verify_followings(self, owner_username, username):
        """Verify following tab data"""
        self.wait_until_displayed(self.constants.FOLLOWING_TAB_XPATH.format(username=owner_username.lower())).click()
        followings = self.driver.find_elements(by=By.XPATH, value=self.constants.FOLLOWERS_LIST_XPATH)
        following_nicks = [follower.text.strip() for follower in followings]
        assert username.lower() in following_nicks
